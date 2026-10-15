#!/usr/bin/env python3
"""Build README.md from data/index.json, and check the index against the live Hub.

    python3 scripts/index.py build   # regenerate README.md
    python3 scripts/index.py check   # list Hub repos missing from the index, and index ids missing from the Hub

Stdlib only. `check` also verifies GitHub repos are public, using `gh` if it is on PATH.
"""
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "index.json"
README = ROOT / "README.md"

HF = "https://huggingface.co"
URL = {
    "models": lambda i: f"{HF}/{i}",
    "datasets": lambda i: f"{HF}/datasets/{i}",
    "spaces": lambda i: f"{HF}/spaces/{i}",
    "repos": lambda i: f"https://github.com/{i}",
}
COLS = [("models", "Model"), ("datasets", "Dataset"), ("spaces", "Space"), ("repos", "Repo"), ("blogs", "Blog")]


def load():
    return json.loads(DATA.read_text())


def short(i):
    return i.split("/", 1)[1]


def cell(project, key):
    items = project.get(key) or []
    if key == "blogs":
        return "<br>".join(f"[{b['title']}]({b['url']})" for b in items) or "—"
    links = [f"[{short(i)}]({URL[key](i)})" for i in items]
    if links and key == "datasets" and project.get("datasets_inferred"):
        links[-1] += " *(inferred)*"
    return "<br>".join(links) or "—"


def anchor(title):
    keep = "".join(c for c in title.lower() if c.isalnum() or c in " -")
    return keep.replace(" ", "-")


def build():
    d = load()
    themes = d["themes"]
    models = [(t, p, m) for t in themes for p in t["projects"] for m in p.get("models", [])]
    out = [
        "# Hugging Face Releases Index",
        "",
        "The models, datasets, Spaces and blog posts I have published on Hugging Face "
        f"([`{d['hf_user']}`]({HF}/{d['hf_user']})), indexed by theme rather than by Hub repo type. "
        "Each project row links its model, its training data, its demo, its GitHub repo and any write-up.",
        "",
        f"**Snapshot:** {d['snapshot']} · "
        + " · ".join(f"{v} {k}" for k, v in d["counts_at_snapshot"].items())
        + " · Machine-readable: [`data/index.json`](data/index.json)",
        "",
        "## Models at a glance",
        "",
        "| Model | Theme | Base | Status |",
        "| --- | --- | --- | --- |",
    ]
    for t, p, m in models:
        out.append(
            f"| [{short(m)}]({URL['models'](m)}) | [{t['title']}](#{anchor(t['title'])}) "
            f"| {p.get('base_model', '—')} | {p.get('status', '—')} |"
        )
    out += ["", "## Themes", ""]
    out += [f"- [{t['title']}](#{anchor(t['title'])})" for t in themes]
    for t in themes:
        out += ["", f"## {t['title']}", "", t["summary"]]
        if t.get("subindex"):
            out += ["", f"Sub-index: [{short(t['subindex'])}]({URL['repos'](t['subindex'])})"]
        used = [(k, h) for k, h in COLS if any(p.get(k) for p in t["projects"])]
        out += [
            "",
            "| Project | " + " | ".join(h for _, h in used) + " |",
            "| --- | " + " | ".join("---" for _ in used) + " |",
        ]
        for p in t["projects"]:
            name = f"**{p['title']}**<br><sub>{p['summary']}</sub>"
            out.append(f"| {name} | " + " | ".join(cell(p, k) for k, _ in used) + " |")
        notes = [f"- **{p['title']}:** {p['notes']}" for p in t["projects"] if p.get("notes")]
        if notes:
            out += [""] + notes
    out += ["", "## Related indexes", ""]
    out += [f"- [{s['title']}]({URL['repos'](s['repo'])})" for s in d["subindexes"]]
    out += [
        "",
        "---",
        "",
        "Generated from `data/index.json` by `scripts/index.py build`. Edit the JSON, not this file.",
        "",
    ]
    README.write_text("\n".join(out))
    print(f"wrote {README.relative_to(ROOT)}: {len(models)} models, {len(themes)} themes")


def hub(kind, user):
    # sort=lastModified: the unsorted full=true listing has silently dropped new repos (seen 2026-10-15).
    url = f"{HF}/api/{kind}?author={user}&limit=1000&sort=lastModified&direction=-1"
    with urllib.request.urlopen(url, timeout=60) as r:
        return {x["id"] for x in json.load(r) if not x.get("private")}


def check():
    d = load()
    indexed = {k: set() for k in ("models", "datasets", "spaces", "repos")}
    for t in d["themes"]:
        for p in t["projects"]:
            for k in indexed:
                indexed[k].update(p.get(k, []))
    problems = 0
    for k in ("models", "datasets", "spaces"):
        live = hub(k, d["hf_user"])
        missing, dead = sorted(live - indexed[k]), sorted(indexed[k] - live)
        print(f"{k}: {len(live)} on Hub, {len(indexed[k])} indexed")
        for i in missing:
            print(f"  NOT INDEXED  {URL[k](i)}")
        for i in dead:
            print(f"  NOT ON HUB   {i}")
        problems += len(missing) + len(dead)
    try:
        for r in sorted(indexed["repos"]):
            vis = subprocess.run(["gh", "repo", "view", r, "--json", "visibility", "-q", ".visibility"],
                                 capture_output=True, text=True).stdout.strip()
            if vis != "PUBLIC":
                print(f"  REPO NOT PUBLIC  {r} ({vis or 'not found'})")
                problems += 1
    except FileNotFoundError:
        print("gh not on PATH; skipped GitHub visibility check")
    print("OK" if not problems else f"{problems} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "build":
        build()
    elif cmd == "check":
        sys.exit(check())
    else:
        sys.exit(__doc__)
