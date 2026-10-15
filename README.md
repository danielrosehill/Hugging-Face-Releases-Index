# Hugging Face Releases Index

The models, datasets, Spaces and blog posts I have published on Hugging Face ([`danielrosehill`](https://huggingface.co/danielrosehill)), indexed by theme rather than by Hub repo type. Each project row links its model, its training data, its demo, its GitHub repo and any write-up.

**Snapshot:** 2026-10-15 · 17 models · 72 datasets · 56 spaces · 2 blogs · Machine-readable: [`data/index.json`](data/index.json)

## Models at a glance

| Model | Theme | Base | Status |
| --- | --- | --- | --- |
| [Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching) | [English-Hebrew code-switching](#english-hebrew-code-switching) | nvidia/parakeet-tdt-0.6b-v2 | released |
| [hebrew-latin-token-classifier](https://huggingface.co/danielrosehill/hebrew-latin-token-classifier) | [English-Hebrew code-switching](#english-hebrew-code-switching) | FacebookAI/xlm-roberta-base | released |
| [Whisper-Hebrish](https://huggingface.co/danielrosehill/Whisper-Hebrish) | [English-Hebrew code-switching](#english-hebrew-code-switching) | openai/whisper-large-v3-turbo | superseded |
| [daniel_whisper_finetune_tiny_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_tiny_v2) | [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper) | openai/whisper-* | released |
| [daniel_whisper_finetune_base_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_base_v2) | [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper) | openai/whisper-* | released |
| [daniel_whisper_finetune_small_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_small_v2) | [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper) | openai/whisper-* | released |
| [daniel_whisper_finetune_medium_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_medium_v2) | [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper) | openai/whisper-* | released |
| [daniel_whisper_finetune_large_v3_turbo_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_large_v3_turbo_v2) | [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper) | openai/whisper-* | released |
| [daniel_whisper_acft_tiny_v2](https://huggingface.co/danielrosehill/daniel_whisper_acft_tiny_v2) | [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper) | — | released |
| [daniel_whisper_acft_base_v2](https://huggingface.co/danielrosehill/daniel_whisper_acft_base_v2) | [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper) | — | released |
| [daniel_whisper_acft_small_v2](https://huggingface.co/danielrosehill/daniel_whisper_acft_small_v2) | [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper) | — | released |
| [Voice-Note-Intent-Classifier](https://huggingface.co/danielrosehill/Voice-Note-Intent-Classifier) | [Text classifiers and routing](#text-classifiers-and-routing) | — | released |
| [jerusalem-poster-detector](https://huggingface.co/danielrosehill/jerusalem-poster-detector) | [Computer vision](#computer-vision) | yolo11 | released |
| [Jerusalem-Images](https://huggingface.co/danielrosehill/Jerusalem-Images) | [Image generation: FLUX LoRAs and photo sets](#image-generation-flux-loras-and-photo-sets) | black-forest-labs/FLUX.1-dev | released |
| [Tel-Aviv-Street-Style](https://huggingface.co/danielrosehill/Tel-Aviv-Street-Style) | [Image generation: FLUX LoRAs and photo sets](#image-generation-flux-loras-and-photo-sets) | black-forest-labs/FLUX.1-dev | released |
| [Dinosaur-Sloth](https://huggingface.co/danielrosehill/Dinosaur-Sloth) | [Image generation: FLUX LoRAs and photo sets](#image-generation-flux-loras-and-photo-sets) | black-forest-labs/FLUX.1-dev | released |
| [Herman-Poppleberry](https://huggingface.co/danielrosehill/Herman-Poppleberry) | [Image generation: FLUX LoRAs and photo sets](#image-generation-flux-loras-and-photo-sets) | black-forest-labs/FLUX.1-dev | released |

## Themes

- [English-Hebrew code-switching](#english-hebrew-code-switching)
- [Personal ASR fine-tunes (Whisper)](#personal-asr-fine-tunes-whisper)
- [Text classifiers and routing](#text-classifiers-and-routing)
- [Computer vision](#computer-vision)
- [Image generation: FLUX LoRAs and photo sets](#image-generation-flux-loras-and-photo-sets)
- [Speech and audio evaluations](#speech-and-audio-evaluations)
- [Transcript cleanup and voice context](#transcript-cleanup-and-voice-context)
- [Israel and Jerusalem data](#israel-and-jerusalem-data)
- [Geopolitics, OSINT and forecasting](#geopolitics-osint-and-forecasting)
- [Sustainability and impact data](#sustainability-and-impact-data)
- [System prompts and agent configurations](#system-prompts-and-agent-configurations)
- [LLM experiments, pricing and taxonomies](#llm-experiments-pricing-and-taxonomies)
- [Reference data and taxonomies](#reference-data-and-taxonomies)
- [Other Spaces](#other-spaces)

## English-Hebrew code-switching

ASR and text models for English speech and text that contain Hebrew words, plus the datasets they were trained on.

Sub-index: [English-Hebrew-Code-Switching-Index](https://github.com/danielrosehill/English-Hebrew-Code-Switching-Index)

| Project | Model | Dataset | Space | Repo |
| --- | --- | --- | --- | --- |
| **Parakeet TDT 0.6B v2 code-switching fine-tune**<br><sub>Parakeet v2 fine-tuned on one speaker reading English sentences with Hebrew words. Ships NeMo and GGUF weights.</sub> | [Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching](https://huggingface.co/danielrosehill/Parakeet-TDT-0.6B-v2-English-Hebrew-Codeswitching) | [Read-Aloud-Voice-Sentences](https://huggingface.co/datasets/danielrosehill/Read-Aloud-Voice-Sentences)<br>[English-Hebrew-Codeswitching-Sentences](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Codeswitching-Sentences) | [English-Hebrew-Codeswitching-Parakeet-Demo](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Parakeet-Demo)<br>[English-Hebrew-Codeswitching-Browser](https://huggingface.co/spaces/danielrosehill/English-Hebrew-Codeswitching-Browser) | [English-Hebrew-Codeswitching-Parakeet-Finetune](https://github.com/danielrosehill/English-Hebrew-Codeswitching-Parakeet-Finetune)<br>[ASR-Training-Data-Collector](https://github.com/danielrosehill/ASR-Training-Data-Collector) |
| **Hebrew-in-Latin token classifier**<br><sub>XLM-R token classifier that finds romanized Hebrew words inside English text. Span F1 0.941 on a term-disjoint test split.</sub> | [hebrew-latin-token-classifier](https://huggingface.co/danielrosehill/hebrew-latin-token-classifier) | [hebrew-latin-code-switching](https://huggingface.co/datasets/danielrosehill/hebrew-latin-code-switching) | [hebrew-latin-token-classifier](https://huggingface.co/spaces/danielrosehill/hebrew-latin-token-classifier)<br>[hebrew-latin-span-review](https://huggingface.co/spaces/danielrosehill/hebrew-latin-span-review) | [Hebrew-Latin-Token-Classifier](https://github.com/danielrosehill/Hebrew-Latin-Token-Classifier) |
| **Whisper-Hebrish**<br><sub>The first code-switching fine-tune: Whisper large-v3-turbo on English sentences with Hebrew words. Its dataset is superseded and has substring-matched labels (114 of 474 wrong).</sub> | [Whisper-Hebrish](https://huggingface.co/danielrosehill/Whisper-Hebrish) | [English-Hebrew-Mixed-Sentences](https://huggingface.co/datasets/danielrosehill/English-Hebrew-Mixed-Sentences) | [Whisper-Hebrish](https://huggingface.co/spaces/danielrosehill/Whisper-Hebrish) | [Whisper-Fine-Tune-Accuracy-Eval](https://github.com/danielrosehill/Whisper-Fine-Tune-Accuracy-Eval) |

## Personal ASR fine-tunes (Whisper)

Whisper fine-tuned on about an hour of my own voice, for local dictation. Includes FUTO-compatible ACFT variants and the evaluations that compared them with commercial APIs.

| Project | Model | Dataset | Space | Repo |
| --- | --- | --- | --- | --- |
| **Whisper fine-tunes v2 (tiny to large-v3-turbo)**<br><sub>Five sizes fine-tuned on about 1 hour of my voice with technical vocabulary. GGML and CTranslate2 conversions are included.</sub> | [daniel_whisper_finetune_tiny_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_tiny_v2)<br>[daniel_whisper_finetune_base_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_base_v2)<br>[daniel_whisper_finetune_small_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_small_v2)<br>[daniel_whisper_finetune_medium_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_medium_v2)<br>[daniel_whisper_finetune_large_v3_turbo_v2](https://huggingface.co/danielrosehill/daniel_whisper_finetune_large_v3_turbo_v2) | [Tech-Sentences-For-ASR-Training](https://huggingface.co/datasets/danielrosehill/Tech-Sentences-For-ASR-Training) *(inferred)* | [Whisper-Fine-Tune-Eval](https://huggingface.co/spaces/danielrosehill/Whisper-Fine-Tune-Eval) | [Modal-Whisper-Finetune-Script](https://github.com/danielrosehill/Modal-Whisper-Finetune-Script)<br>[Whisper-Fine-Tune-Accuracy-Eval](https://github.com/danielrosehill/Whisper-Fine-Tune-Accuracy-Eval)<br>[STT-Fine-Tune-Project-Outline](https://github.com/danielrosehill/STT-Fine-Tune-Project-Outline) |
| **Whisper ACFT fine-tunes (FUTO keyboard)**<br><sub>Tiny, base and small fine-tunes in FUTO's ACFT format, for the FUTO Android voice keyboard.</sub> | [daniel_whisper_acft_tiny_v2](https://huggingface.co/danielrosehill/daniel_whisper_acft_tiny_v2)<br>[daniel_whisper_acft_base_v2](https://huggingface.co/danielrosehill/daniel_whisper_acft_base_v2)<br>[daniel_whisper_acft_small_v2](https://huggingface.co/danielrosehill/daniel_whisper_acft_small_v2) | — | — | [whisper-acft](https://github.com/danielrosehill/whisper-acft)<br>[Modal-ACFT-Finetune-Script](https://github.com/danielrosehill/Modal-ACFT-Finetune-Script) |
| **Fine-tune evaluations**<br><sub>Whether the local fine-tunes beat stock Whisper and commercial STT APIs on my voice.</sub> | — | [Whisper-Fine-Tune-One-Shot-Eval](https://huggingface.co/datasets/danielrosehill/Whisper-Fine-Tune-One-Shot-Eval)<br>[STT-Fine-Tune-Eval-101225](https://huggingface.co/datasets/danielrosehill/STT-Fine-Tune-Eval-101225) | [Whisper-Fine-Tune-Eval](https://huggingface.co/spaces/danielrosehill/Whisper-Fine-Tune-Eval) | [Whisper-Fine-Tune-Accuracy-Eval](https://github.com/danielrosehill/Whisper-Fine-Tune-Accuracy-Eval) |
| **Tech Sentences (2026 recording set)**<br><sub>Dictation-style English sentences dense in software, DevOps and AI vocabulary, read aloud by one speaker. Training data for the next personal fine-tune.</sub> | — | [Tech-Sentences](https://huggingface.co/datasets/danielrosehill/Tech-Sentences) | — | — |

- **Whisper fine-tunes v2 (tiny to large-v3-turbo):** The model cards say 'unknown dataset'. The TechVoice dataset matches the described training data but is not confirmed as the source.

## Text classifiers and routing

Small classifiers that route or label text before an LLM sees it.

| Project | Model | Dataset | Space |
| --- | --- | --- | --- |
| **Voice-Note Intent Classifier**<br><sub>Multi-label intent classifier for voice-note transcripts. It routes each note to the right agent or MCP tool.</sub> | [Voice-Note-Intent-Classifier](https://huggingface.co/danielrosehill/Voice-Note-Intent-Classifier) | — | — |
| **Prompt separation**<br><sub>Voice-typed prompt transcripts split into discrete asks and context chunks. A candidate training set for a prompt/context splitter.</sub> | — | [Prompt-Separation](https://huggingface.co/datasets/danielrosehill/Prompt-Separation)<br>[prompt-or-not](https://huggingface.co/datasets/danielrosehill/prompt-or-not) | [Prompt-And-Output-Separator](https://huggingface.co/spaces/danielrosehill/Prompt-And-Output-Separator) |

- **Voice-Note Intent Classifier:** Training dataset not yet published.

## Computer vision

Detection models and image datasets for OCR and recognition tasks.

| Project | Model | Dataset | Space | Repo |
| --- | --- | --- | --- | --- |
| **Jerusalem poster detector**<br><sub>YOLO11 detector for one street-postering campaign in central Jerusalem, trained on geotagged street photos.</sub> | [jerusalem-poster-detector](https://huggingface.co/danielrosehill/jerusalem-poster-detector) | [jerusalem-poster-detection](https://huggingface.co/datasets/danielrosehill/jerusalem-poster-detection) | — | — |
| **Whiteboards**<br><sub>Single-author whiteboard photos for testing handwritten OCR in vision-language models.</sub> | — | [Whiteboards](https://huggingface.co/datasets/danielrosehill/Whiteboards) | [Nano-Banana-Sketch-Cleanup](https://huggingface.co/spaces/danielrosehill/Nano-Banana-Sketch-Cleanup) | [Sample-Whiteboards](https://github.com/danielrosehill/Sample-Whiteboards) |
| **NVR entity recognition**<br><sub>Labelled frames from home security cameras (NVR), for entity recognition.</sub> | — | [NVR-Entity-Recognition-Experiment](https://huggingface.co/datasets/danielrosehill/NVR-Entity-Recognition-Experiment) | — | — |
| **Accidental and low-quality photos**<br><sub>Accidental and blurry camera-roll shots, for training a filter that finds them.</sub> | — | [accidental-and-low-quality-photos](https://huggingface.co/datasets/danielrosehill/accidental-and-low-quality-photos) | — | — |

## Image generation: FLUX LoRAs and photo sets

FLUX.1-dev LoRAs trained on Replicate, the photo sets behind them, and text-to-image evaluations.

| Project | Model | Dataset | Repo |
| --- | --- | --- | --- |
| **Jerusalem and Tel Aviv LoRAs**<br><sub>LoRAs for realistic streetscapes of West Jerusalem and Tel Aviv street style.</sub> | [Jerusalem-Images](https://huggingface.co/danielrosehill/Jerusalem-Images)<br>[Tel-Aviv-Street-Style](https://huggingface.co/danielrosehill/Tel-Aviv-Street-Style) | [Jerusalem-Streetscapes](https://huggingface.co/datasets/danielrosehill/Jerusalem-Streetscapes)<br>[Tel-Aviv-Pics](https://huggingface.co/datasets/danielrosehill/Tel-Aviv-Pics) *(inferred)* | — |
| **Character LoRAs (My Weird Prompts)**<br><sub>LoRAs for Corn the sloth and Herman Poppleberry, the My Weird Prompts podcast characters.</sub> | [Dinosaur-Sloth](https://huggingface.co/danielrosehill/Dinosaur-Sloth)<br>[Herman-Poppleberry](https://huggingface.co/danielrosehill/Herman-Poppleberry) | [Corn-The-Sloth](https://huggingface.co/datasets/danielrosehill/Corn-The-Sloth)<br>[Corn-Training-Set](https://huggingface.co/datasets/danielrosehill/Corn-Training-Set) | [Corn-The-Sloth-Public](https://github.com/danielrosehill/Corn-The-Sloth-Public)<br>[3D-Models](https://github.com/danielrosehill/3D-Models) |
| **Israel photo sets**<br><sub>Captioned photographs of Israeli cities, high-rise development and Hebrew signage.</sub> | — | [Israel-Photos](https://huggingface.co/datasets/danielrosehill/Israel-Photos)<br>[Jerusalem-High-Rise-Development](https://huggingface.co/datasets/danielrosehill/Jerusalem-High-Rise-Development)<br>[Hebrew-Language-Signage](https://huggingface.co/datasets/danielrosehill/Hebrew-Language-Signage) | — |
| **Text-to-image evaluations**<br><sub>How well text-to-image models render Hebrew, plus a library of test prompts.</sub> | — | [Hebrew-Image-Eval-111225](https://huggingface.co/datasets/danielrosehill/Hebrew-Image-Eval-111225)<br>[Text-To-Image-Test-Prompts](https://huggingface.co/datasets/danielrosehill/Text-To-Image-Test-Prompts) | [Text-To-Image-Test-Prompts](https://github.com/danielrosehill/Text-To-Image-Test-Prompts) |

- **Jerusalem and Tel Aviv LoRAs:** The Jerusalem-Images card describes its training set as West Jerusalem streetscapes from summer 2025. The dataset pairing is inferred from that description.

## Speech and audio evaluations

Benchmarks of local and cloud STT, and tests of audio understanding in multimodal models.

Sub-index: [Speech-And-ASR-Evaluations](https://github.com/danielrosehill/Speech-And-ASR-Evaluations)

| Project | Dataset | Space | Repo |
| --- | --- | --- | --- |
| **Voice-note STT evaluations**<br><sub>Real voice notes, clean and noisy, used to compare STT services.</sub> | [STT-Voice-Notes-Evals](https://huggingface.co/datasets/danielrosehill/STT-Voice-Notes-Evals)<br>[Voice-Note-Audio](https://huggingface.co/datasets/danielrosehill/Voice-Note-Audio)<br>[Noisy-Voice-Notes](https://huggingface.co/datasets/danielrosehill/Noisy-Voice-Notes)<br>[Small-STT-Eval-Audio-Dataset](https://huggingface.co/datasets/danielrosehill/Small-STT-Eval-Audio-Dataset) | [STT-Comparison](https://huggingface.co/spaces/danielrosehill/STT-Comparison)<br>[Local-STT-Eval-One-Sample](https://huggingface.co/spaces/danielrosehill/Local-STT-Eval-One-Sample) | [STT-Voice-Note-Evaluation](https://github.com/danielrosehill/STT-Voice-Note-Evaluation) |
| **Speaking pace and background noise**<br><sub>How speaking rate (WPM) and background noise affect Whisper accuracy.</sub> | [ASR-WPM-And-Background-Noise-Eval](https://huggingface.co/datasets/danielrosehill/ASR-WPM-And-Background-Noise-Eval) | — | [Whisper-WPM-Background-Noise-Eval](https://github.com/danielrosehill/Whisper-WPM-Background-Noise-Eval) |
| **Podcast ASR benchmark**<br><sub>Local and cloud models compared on one podcast episode.</sub> | [Podcast-ASR-Evaluation](https://huggingface.co/datasets/danielrosehill/Podcast-ASR-Evaluation) | [Single-Podcast-ASR-Eval](https://huggingface.co/spaces/danielrosehill/Single-Podcast-ASR-Eval) | — |
| **Local STT on AMD GPU**<br><sub>13 local STT models benchmarked through Handy on an AMD GPU.</sub> | — | [Single-Shot-ASR-Eval](https://huggingface.co/spaces/danielrosehill/Single-Shot-ASR-Eval) | [Local-ASR-STT-Benchmark](https://github.com/danielrosehill/Local-ASR-STT-Benchmark) |
| **Audio understanding**<br><sub>137 test prompts for audio understanding in multimodal models, plus an eval of MP3 bitrate against transcription accuracy.</sub> | [Audio-Understanding-Test-Set](https://huggingface.co/datasets/danielrosehill/Audio-Understanding-Test-Set)<br>[Audio-Understanding-Bitrate-Eval-0426](https://huggingface.co/datasets/danielrosehill/Audio-Understanding-Bitrate-Eval-0426) | [Audio-Understanding-Experiment](https://huggingface.co/spaces/danielrosehill/Audio-Understanding-Experiment) | [Audio-Understanding-Bitrate-Eval-0426](https://github.com/danielrosehill/Audio-Understanding-Bitrate-Eval-0426) |
| **Audio tooling demos**<br><sub>Baby-noise removal compared by STT output, audio-to-SRT with diarization, Hebrew TTS providers compared, and a browser of Whisper apps.</sub> | — | [Deepnet-Baby-Noise-Scrub](https://huggingface.co/spaces/danielrosehill/Deepnet-Baby-Noise-Scrub)<br>[Audio-To-Subtitles](https://huggingface.co/spaces/danielrosehill/Audio-To-Subtitles)<br>[Hebrew-TTS-Samples](https://huggingface.co/spaces/danielrosehill/Hebrew-TTS-Samples)<br>[Interesting-Whisper-Projects](https://huggingface.co/spaces/danielrosehill/Interesting-Whisper-Projects) | [Awesome-Whisper-Apps](https://github.com/danielrosehill/Awesome-Whisper-Apps) |

## Transcript cleanup and voice context

Turning raw dictation into usable text, and voice recordings into structured context for AI.

| Project | Dataset | Space | Repo |
| --- | --- | --- | --- |
| **Transcript cleanup**<br><sub>A fine-tuning set for STT cleanup models, prompts for reformatting dictated text, and demos.</sub> | [Transcription-Cleanup-Trainer](https://huggingface.co/datasets/danielrosehill/Transcription-Cleanup-Trainer)<br>[Speech-To-Text-System-Prompts-2](https://huggingface.co/datasets/danielrosehill/Speech-To-Text-System-Prompts-2)<br>[Text-Transformation-Prompts-300525](https://huggingface.co/datasets/danielrosehill/Text-Transformation-Prompts-300525) | [Basic-STT-Transcript-Cleanup](https://huggingface.co/spaces/danielrosehill/Basic-STT-Transcript-Cleanup)<br>[Text-Transformation-Model](https://huggingface.co/spaces/danielrosehill/Text-Transformation-Model)<br>[BLUF-Email-Formatter](https://huggingface.co/spaces/danielrosehill/BLUF-Email-Formatter) | [Text-Cleanup-Fine-Tuning-Set](https://github.com/danielrosehill/Text-Cleanup-Fine-Tuning-Set)<br>[STT-Basic-Cleanup-System-Prompt](https://github.com/danielrosehill/STT-Basic-Cleanup-System-Prompt) |
| **Voice context generation**<br><sub>Narrated voice recordings turned into structured context data for agents.</sub> | [Sample-Voice-Context-Data](https://huggingface.co/datasets/danielrosehill/Sample-Voice-Context-Data)<br>[Career-Data-Context-Repo](https://huggingface.co/datasets/danielrosehill/Career-Data-Context-Repo)<br>[Software-Wish-List-Context-Data](https://huggingface.co/datasets/danielrosehill/Software-Wish-List-Context-Data) | [Context-Cruncher](https://huggingface.co/spaces/danielrosehill/Context-Cruncher)<br>[AI-Context-Generation-Interviews](https://huggingface.co/spaces/danielrosehill/AI-Context-Generation-Interviews) | [Context-Cruncher](https://github.com/danielrosehill/Context-Cruncher) |

## Israel and Jerusalem data

Civic, environmental and market datasets about Israel.

| Project | Dataset | Space | Repo | Blog |
| --- | --- | --- | --- | --- |
| **Jerusalem air quality: weekday vs Shabbat**<br><sub>Twelve months of 5-minute readings from 12 Jerusalem stations, with Shabbat treated as a natural experiment.</sub> | [Jerusalem-Air-Quality-Shabbat](https://huggingface.co/datasets/danielrosehill/Jerusalem-Air-Quality-Shabbat) | [Jerusalem-Air-Quality-Shabbat-Findings](https://huggingface.co/spaces/danielrosehill/Jerusalem-Air-Quality-Shabbat-Findings) | — | [How Shabbat Cleans Jerusalem's Air (For One Day A Week)](https://huggingface.co/blog/danielrosehill/jerusalem-shabbat-air) |
| **Israel Open Data Catalogue**<br><sub>A bilingual snapshot of the entire data.gov.il catalogue.</sub> | [Israel-Open-Data-Catalogue](https://huggingface.co/datasets/danielrosehill/Israel-Open-Data-Catalogue) | — | [Israel-Open-Data-Catalogue-Translations](https://github.com/danielrosehill/Israel-Open-Data-Catalogue-Translations) | — |
| **Civil defence**<br><sub>Home Front Command alerting zones and Jerusalem public shelter locations.</sub> | [Israel-Alerting-Zones](https://huggingface.co/datasets/danielrosehill/Israel-Alerting-Zones)<br>[Jerusalem-Emergency-Shelters-0925](https://huggingface.co/datasets/danielrosehill/Jerusalem-Emergency-Shelters-0925) | — | — | — |
| **Ivory computer parts catalogue**<br><sub>A February 2026 price snapshot from Ivory.co.il, an Israeli electronics retailer.</sub> | [Ivory-Catalog-020226](https://huggingface.co/datasets/danielrosehill/Ivory-Catalog-020226) | — | — | — |

## Geopolitics, OSINT and forecasting

Multi-agent forecasting runs and open-source conflict data.

| Project | Dataset | Space | Repo |
| --- | --- | --- | --- |
| **Geopol Forecaster**<br><sub>Structured predictions from multi-agent wargaming runs, with accuracy tracking.</sub> | [Geopol-Forecaster-Predictions](https://huggingface.co/datasets/danielrosehill/Geopol-Forecaster-Predictions) | [Geopolitical-Predictions](https://huggingface.co/spaces/danielrosehill/Geopolitical-Predictions)<br>[Geopol-Forecast-Iran-Israel](https://huggingface.co/spaces/danielrosehill/Geopol-Forecast-Iran-Israel) | [Geopol-Forecaster](https://github.com/danielrosehill/Geopol-Forecaster)<br>[Geopol-Forecasts-Index](https://github.com/danielrosehill/Geopol-Forecasts-Index) |
| **Iran-Israel war 2026 OSINT**<br><sub>Iranian missile and drone attack waves against Israel and US/coalition targets.</sub> | [Iran-Israel-War-2026](https://huggingface.co/datasets/danielrosehill/Iran-Israel-War-2026) | — | [Iran-Israel-War-2026-OSINT-Data](https://github.com/danielrosehill/Iran-Israel-War-2026-OSINT-Data) |
| **Analyst agents**<br><sub>A multi-agent UN simulation, satellite-imagery analysis, and geopolitical system prompts.</sub> | [Geopolitical-System-Prompts](https://huggingface.co/datasets/danielrosehill/Geopolitical-System-Prompts) | [Agent-UN](https://huggingface.co/spaces/danielrosehill/Agent-UN)<br>[SATINT-Analyst](https://huggingface.co/spaces/danielrosehill/SATINT-Analyst) | — |

## Sustainability and impact data

Monetised GHG emissions and IFVI value factors.

| Project | Dataset | Space | Repo |
| --- | --- | --- | --- |
| **Global Value Factor Database (IFVI)**<br><sub>A refactor of IFVI's value factors, with explorers. V1 is deprecated in favour of V2.</sub> | [Global-Value-Factor-Database-Refactor-V2](https://huggingface.co/datasets/danielrosehill/Global-Value-Factor-Database-Refactor-V2)<br>[ifvi_valuefactors_deriv](https://huggingface.co/datasets/danielrosehill/ifvi_valuefactors_deriv) | [GVFD-Navigator](https://huggingface.co/spaces/danielrosehill/GVFD-Navigator)<br>[GVFD-Explorer](https://huggingface.co/spaces/danielrosehill/GVFD-Explorer) | [GVFD-Explorer-Chatbot-V2](https://github.com/danielrosehill/GVFD-Explorer-Chatbot-V2) |
| **Monetised GHG emissions**<br><sub>An emissions data pipeline, with calculators that weigh monetised emissions against profitability.</sub> | [GHG-Emissions-Data](https://huggingface.co/datasets/danielrosehill/GHG-Emissions-Data) | [Monetised-GHG-Emissions-Calculator](https://huggingface.co/spaces/danielrosehill/Monetised-GHG-Emissions-Calculator)<br>[ghg-emissions-viz](https://huggingface.co/spaces/danielrosehill/ghg-emissions-viz) | [GHG-Emissions-Data-Pipeline](https://github.com/danielrosehill/GHG-Emissions-Data-Pipeline)<br>[Monetised-GHG-Emissions](https://github.com/danielrosehill/Monetised-GHG-Emissions) |
| **Pay-for-outcomes instruments**<br><sub>Standardized social impact bond data based on Government Outcomes Lab.</sub> | [pay-for-outcomes-instruments](https://huggingface.co/datasets/danielrosehill/pay-for-outcomes-instruments) | — | — |

## System prompts and agent configurations

Prompt libraries and agent networks, with the tools that generate and reformat them.

| Project | Dataset | Space | Repo | Blog |
| --- | --- | --- | --- | --- |
| **System prompt library**<br><sub>The main library: a live version, an August 2025 snapshot, and topical subsets.</sub> | [System-Prompt-Library](https://huggingface.co/datasets/danielrosehill/System-Prompt-Library)<br>[System-Prompt-Library-030825](https://huggingface.co/datasets/danielrosehill/System-Prompt-Library-030825)<br>[General-Purpose-System-Prompts](https://huggingface.co/datasets/danielrosehill/General-Purpose-System-Prompts)<br>[Prompt-Eng-System-Prompts](https://huggingface.co/datasets/danielrosehill/Prompt-Eng-System-Prompts)<br>[Email-Management-System-Prompts](https://huggingface.co/datasets/danielrosehill/Email-Management-System-Prompts)<br>[Data-Utils-System-Prompts](https://huggingface.co/datasets/danielrosehill/Data-Utils-System-Prompts)<br>[Career-Related-System-Prompts](https://huggingface.co/datasets/danielrosehill/Career-Related-System-Prompts)<br>[Writing-System-Prompts](https://huggingface.co/datasets/danielrosehill/Writing-System-Prompts) | [System-Prompt-Factory](https://huggingface.co/spaces/danielrosehill/System-Prompt-Factory)<br>[System-Prompt-Depersonaliser](https://huggingface.co/spaces/danielrosehill/System-Prompt-Depersonaliser)<br>[System-Prompt-Reformatter](https://huggingface.co/spaces/danielrosehill/System-Prompt-Reformatter)<br>[Assistant-Config-Library](https://huggingface.co/spaces/danielrosehill/Assistant-Config-Library)<br>[AI-Assistants-Library](https://huggingface.co/spaces/danielrosehill/AI-Assistants-Library) | [System-Prompt-Library](https://github.com/danielrosehill/System-Prompt-Library)<br>[System-Prompt-Factory](https://github.com/danielrosehill/System-Prompt-Factory)<br>[Email-Management-System-Prompts](https://github.com/danielrosehill/Email-Management-System-Prompts)<br>[Writing-System-Prompts](https://github.com/danielrosehill/Writing-System-Prompts) | — |
| **Agent networks**<br><sub>A code-generation agent network and a support-agent network.</sub> | [Code-Gen-Agents-0925](https://huggingface.co/datasets/danielrosehill/Code-Gen-Agents-0925)<br>[Narcissistic-Abuse-Support-Configs](https://huggingface.co/datasets/danielrosehill/Narcissistic-Abuse-Support-Configs) | [Code-Gen-Agents-Network](https://huggingface.co/spaces/danielrosehill/Code-Gen-Agents-Network)<br>[Code-Gen-Agent-Prompt-Assistant](https://huggingface.co/spaces/danielrosehill/Code-Gen-Agent-Prompt-Assistant)<br>[Claude-Agent-Picker-Idea](https://huggingface.co/spaces/danielrosehill/Claude-Agent-Picker-Idea) | — | — |
| **Claude Code slash commands**<br><sub>Browsers for my Claude Code slash commands, general and Linux-desktop.</sub> | — | [Claude-Code-Slash-Commands](https://huggingface.co/spaces/danielrosehill/Claude-Code-Slash-Commands)<br>[Claude-Code-Slash-Commands-Linux-Desktop](https://huggingface.co/spaces/danielrosehill/Claude-Code-Slash-Commands-Linux-Desktop) | — | [A Voluntary Code Of Practice For Responsible Agent Skill Development](https://huggingface.co/blog/danielrosehill/responsible-agent-skill-dev) |
| **Text style transformers**<br><sub>Shakespearean rewrites, human-to-AI style conversion, a pen-pal interface and prompt-to-podcast scripts.</sub> | [Shakespearean-Text-Transformation-Prompts](https://huggingface.co/datasets/danielrosehill/Shakespearean-Text-Transformation-Prompts) | [Shakespeare-AI](https://huggingface.co/spaces/danielrosehill/Shakespeare-AI)<br>[Human-To-AI-Text-Converter](https://huggingface.co/spaces/danielrosehill/Human-To-AI-Text-Converter)<br>[Penpal-AI-Interface](https://huggingface.co/spaces/danielrosehill/Penpal-AI-Interface)<br>[Prompt-To-Podcast-Script](https://huggingface.co/spaces/danielrosehill/Prompt-To-Podcast-Script)<br>[EQ-Template-Generator](https://huggingface.co/spaces/danielrosehill/EQ-Template-Generator) | — | — |

## LLM experiments, pricing and taxonomies

One-off experiments on LLM behaviour, API price snapshots, and a map of multimodal AI.

| Project | Dataset | Space | Repo |
| --- | --- | --- | --- |
| **Output length and prompt structure**<br><sub>Maximum single-output length for code generation, whether prompt structure matters, and whether one prompt can produce a book.</sub> | [Long-Prompt-Experiment](https://huggingface.co/datasets/danielrosehill/Long-Prompt-Experiment)<br>[Single-Prompt-Book](https://huggingface.co/datasets/danielrosehill/Single-Prompt-Book)<br>[ChatGPT-AI-Vs-API](https://huggingface.co/datasets/danielrosehill/ChatGPT-AI-Vs-API) | [llm-long-codegen-experiment](https://huggingface.co/spaces/danielrosehill/llm-long-codegen-experiment)<br>[Max-Output-Tokens-Analysis-0225](https://huggingface.co/spaces/danielrosehill/Max-Output-Tokens-Analysis-0225)<br>[Single-Shot-Brevity-Training](https://huggingface.co/spaces/danielrosehill/Single-Shot-Brevity-Training) | — |
| **LLM API pricing**<br><sub>Point-in-time OpenRouter pricing, and 218 tool-calling LLMs compared on cost and context.</sub> | [Open-Router-API-Pricing-Analysis](https://huggingface.co/datasets/danielrosehill/Open-Router-API-Pricing-Analysis) | [Agentic-LLM-Price-Comparisons](https://huggingface.co/spaces/danielrosehill/Agentic-LLM-Price-Comparisons) | — |
| **Multimodal AI taxonomy**<br><sub>A structured map of multimodal model capabilities by input and output modality.</sub> | [multimodal-ai-taxonomy](https://huggingface.co/datasets/danielrosehill/multimodal-ai-taxonomy) | [Multimodal-AI-Taxonomy](https://huggingface.co/spaces/danielrosehill/Multimodal-AI-Taxonomy)<br>[The-Agentic-Symphony](https://huggingface.co/spaces/danielrosehill/The-Agentic-Symphony) | [Multimodal-AI-Taxonomy](https://github.com/danielrosehill/Multimodal-AI-Taxonomy) |
| **My Weird Prompts podcast corpus**<br><sub>AI-generated podcast episodes and a navigator for the corpus.</sub> | [ai-generated-podcast-episodes](https://huggingface.co/datasets/danielrosehill/ai-generated-podcast-episodes) | [mwp-dataset-navigator](https://huggingface.co/spaces/danielrosehill/mwp-dataset-navigator) | — |
| **Writing-style corpus**<br><sub>My old blog posts, used to fine-tune a writing-style generator.</sub> | [Blog-Posts](https://huggingface.co/datasets/danielrosehill/Blog-Posts) | — | — |

## Reference data and taxonomies

Lookup tables and classification schemes.

| Project | Dataset | Repo |
| --- | --- | --- |
| **HomeGoods Taxonomy**<br><sub>A hierarchical classification of household and small-business physical goods, with handling attributes.</sub> | [homegoods-taxonomy](https://huggingface.co/datasets/danielrosehill/homegoods-taxonomy) | [HomeGoods-Taxonomy](https://github.com/danielrosehill/HomeGoods-Taxonomy) |
| **Storage container dimensions**<br><sub>Planning-grade volumes for European and North American warehouse plastic containers.</sub> | [storage-container-dimensions](https://huggingface.co/datasets/danielrosehill/storage-container-dimensions) | [Eurobox_Poster](https://github.com/danielrosehill/Eurobox_Poster) |
| **ISO 3166 / ISO 4217 consolidated**<br><sub>A country-to-currency lookup table.</sub> | [ISO-3166-4217-Consolidated](https://huggingface.co/datasets/danielrosehill/ISO-3166-4217-Consolidated) | [ISO3166-4217-Consolidated](https://github.com/danielrosehill/ISO3166-4217-Consolidated) |
| **Point-in-time catalogues**<br><sub>Zapier's integrations list (August 2025) and my GitHub repos (August 2025).</sub> | [Zapier-Integrations-260825](https://huggingface.co/datasets/danielrosehill/Zapier-Integrations-260825)<br>[github-repos-100825](https://huggingface.co/datasets/danielrosehill/github-repos-100825) | — |

## Other Spaces

Spaces that do not belong to any theme above.

| Project | Space |
| --- | --- |
| **Lisdexamfetamine split-dose modeller**<br><sub>Models split-dose Vyvanse protocols.</sub> | [Lisdexamfetamine-Split-Dose-Modeller](https://huggingface.co/spaces/danielrosehill/Lisdexamfetamine-Split-Dose-Modeller) |
| **Project showcases**<br><sub>Gemini vibe-coded proofs of concept, and an older navigable index of AI projects.</sub> | [Gemini-Vibe-Coded-POCs](https://huggingface.co/spaces/danielrosehill/Gemini-Vibe-Coded-POCs)<br>[AI-Project-Index](https://huggingface.co/spaces/danielrosehill/AI-Project-Index) |

## Related indexes

- [Subindices (index of indexes)](https://github.com/danielrosehill/Subindices)
- [AI Projects Index](https://github.com/danielrosehill/AI-Projects-Index)
- [Data Projects Index](https://github.com/danielrosehill/Data-Projects-Index)
- [English-Hebrew Code-Switching Index](https://github.com/danielrosehill/English-Hebrew-Code-Switching-Index)
- [Speech Tech Index](https://github.com/danielrosehill/Speech-Tech-Index)
- [Speech and ASR Evaluations](https://github.com/danielrosehill/Speech-And-ASR-Evaluations)

---

Generated from `data/index.json` by `scripts/index.py build`. Edit the JSON, not this file.
