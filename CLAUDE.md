# CLAUDE.md — Hugging-Face-Releases-Index

Public thematic index of everything Daniel has published on Hugging Face (user `danielrosehill`): models, datasets, Spaces and HF blog posts. Each one is linked to its companion GitHub repo where one exists. Created 2026-10-15.

## Source of truth

`data/index.json` is the source. `README.md` is **generated** — never edit it by hand.

```bash
python3 scripts/index.py check   # Hub vs index diff + GitHub visibility; exit 1 on any problem
python3 scripts/index.py build   # regenerate README.md
```

Stdlib only, no venv needed. `check` shells out to `gh` for repo visibility.

## Adding a release

1. Run `check`. It prints every public Hub repo that is `NOT INDEXED`.
2. Add the repo to an existing project in `data/index.json`, or add a new project under the right theme. A project groups everything for one piece of work: `models`, `datasets`, `spaces`, `repos`, `blogs`. Training data goes in the same project as the model it trained.
3. Bump `snapshot` and `counts_at_snapshot`. Counts come from `https://huggingface.co/api/users/danielrosehill/overview` (`numModels`, `numDatasets`, `numSpaces`).
4. Run `build`, then `check` again. It must print `OK`. Then commit and push.

## Rules

- **This repo is public and must contain only public things.** Link public GitHub repos only, and never name or describe a private repo, even in `notes`. `check` flags any repo that is not public.
- **Mark guesses.** If the HF card does not name the training dataset and you paired one by description, set `"datasets_inferred": true` and explain in `notes`. That applies today to the Whisper v2 fine-tunes and to the Jerusalem/Tel Aviv LoRAs.
- **Blog posts are not discoverable by API.** `/api/blog?author=` ignores the author filter and returns the global feed (verified 2026-10-15). Scrape the profile page instead:
  `curl -s https://huggingface.co/danielrosehill | grep -oE '/blog/danielrosehill/[A-Za-z0-9._-]+' | sort -u`
- **Listing trap.** The unsorted `api/models?author=…&full=true` listing has silently dropped brand-new repos. `scripts/index.py` sorts by `lastModified`, which returned them.
- HF collections (`/api/collections?owner=danielrosehill`) are mostly bookmarks of *other people's* models. Only "My Models - Classifiers", "My Whisper Fine-Tunes (V2)", "My Whisper ACFT Fine Tunes", "My LORAS", "My Public Audio Datasets" and the code-switching collection are Daniel's own releases. They are useful cross-checks but are not indexed.

## Linked from

These public indexes link here. If you rename this repo, update all of them:

- `Subindices`: an H3 block in the README. Then run `scripts/build-indices-json.py` there. `Index` pulls the list from Subindices.
- `AI-Projects-Index`: the "Related AI Project Indices" list.
- `Data-Projects-Index`: the "Hugging Face Releases" section.
- `Speech-Tech-Index`: end of the "ASR Fine-Tuning" section.
- `English-Hebrew-Code-Switching-Index`: the "Related indexes" table.

## Related

- `English-Hebrew-Code-Switching-Index` is a deeper sub-index of the first theme. Keep the two consistent when code-switching releases change.
- `Development-Project-Index` (2025-11) is an older automated flat dump of GitHub + HF. It is not thematic, has no models, and is not maintained alongside this repo.
