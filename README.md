# Portfolio Product Development

Static GitHub Pages portfolio for University of Antwerp Product Development student work.

The first release is prepared for Bachelor Proef 2025-2026, with assignment pages for Exoskeletons and Circular Sensors. The structure is ready for future courses and year archives.

## Source Content

- `Content/2025-2026/Bachelorproef/Student_List.xlsx`: source spreadsheet with student names, codes, target groups, contexts, and assignment hints.
- `Content/2025-2026/Bachelorproef/Fiche/`: poster/fiche PDFs.
- `Content/2025-2026/Bachelorproef/Eindpresentatie/`: final presentation PDFs and related media.
- `Content/2025-2026/Bachelorproef/Instagram/`: social media visuals.
- `Content/StyleGuide/`: drop University of Antwerp style guide files, logo assets, font information, color references, and usage rules here.
- `Content/metadata/projects.generated.json`: generated, reviewable project data snapshot.

Recommended student folder shape:

```text
student-lastname-firstname-project-slug/
  poster.pdf
  presentation.pdf
  visuals/
    social-01.jpg
    social-02.jpg
```

## Content Model

The public website currently reads from `src/content.js`.

Each project entry includes:

- `id`
- `assignmentId`
- `student`
- bilingual `title`
- bilingual `summary`
- bilingual `context`
- bilingual `targetGroup`
- editable `tags`
- asset paths for thumbnail, poster, presentation, and visuals

This keeps the first version fully static while still making it practical to add an admin-like workflow later through scripts that scan folders and update the data file.

## Generate Project Data

Run this after adding or changing source files:

```bash
/Users/jellesaldien/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/generate_content.py
```

For a public GitHub Pages push without the full student archive, generate with:

```bash
PUBLIC_ASSETS_ONLY=1 /Users/jellesaldien/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/generate_content.py
```

The generator:

- reads `Student_List.xlsx`
- infers assignment pages from project codes such as `EX`, `IEX`, `PEX`, `CS`, `ICS`, and `PCS`
- matches student folders across poster, presentation, and Instagram sections
- renders PDF-based Instagram visuals into PNG previews under `assets/generated/instagram-previews/`
- creates poster previews under `assets/generated/poster-previews/`
- extracts text from poster and presentation PDFs to build editable bilingual project descriptions
- writes `Content/metadata/projects.generated.json`
- updates `src/content.js` for the website

The generated titles, summaries, and tags are a first pass and should be reviewed before publication.

## Local Preview

Because this is a plain static site, it can be opened directly in a browser or served with any small static server.

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Then open `http://127.0.0.1:8000`.

## Suggested Filters

Initial filter vocabulary:

- Assignment: Exoskeletons, Circular Sensors
- Context: healthcare, workplace, mobility, public space, home, education, sports
- Target group: professionals, patients, older adults, children, students, caregivers, citizens
- Design angle: ergonomics, circularity, repairability, data, sustainability, assistive technology
- Technology/material: wearable, sensor, modular, low-impact material, service system

Tags are intentionally editable after the first automatic classification pass.
