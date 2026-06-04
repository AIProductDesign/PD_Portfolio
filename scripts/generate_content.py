from __future__ import annotations

import json
import os
import re
import subprocess
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote

import pandas as pd
from PIL import Image, ImageOps
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = ROOT / "Content" / "2025-2026" / "Bachelorproef"
STUDENT_LIST = CONTENT_ROOT / "Student_List.xlsx"
DESCRIPTION_TSV = CONTENT_ROOT / "Eindpresentatie" / "student_descriptions.tsv"
OUTPUT_JSON = ROOT / "Content" / "metadata" / "projects.generated.json"
OUTPUT_JS = ROOT / "src" / "content.js"
GENERATED_VISUALS = ROOT / "assets" / "generated" / "instagram-previews"
GENERATED_POSTERS = ROOT / "assets" / "generated" / "poster-previews"
GITHUB_FILE_LIMIT_BYTES = 100 * 1024 * 1024
PUBLIC_ASSETS_ONLY = os.environ.get("PUBLIC_ASSETS_ONLY") == "1"
MAX_INSTAGRAM_VISUALS = 4


def clean(value: object) -> str:
    if pd.isna(value):
        return ""
    return str(value).strip()


def normalize(value: str) -> str:
    text = unicodedata.normalize("NFD", value)
    text = "".join(char for char in text if unicodedata.category(char) != "Mn")
    return re.sub(r"[^a-z0-9]", "", text.lower())


def slugify(value: str) -> str:
    text = unicodedata.normalize("NFD", value)
    text = "".join(char for char in text if unicodedata.category(char) != "Mn")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text or "project"


def web_path(path: Path) -> str:
    return quote(path.relative_to(ROOT).as_posix(), safe="/")


def load_student_descriptions() -> dict[str, dict[str, str]]:
    if not DESCRIPTION_TSV.exists():
        return {}
    df = pd.read_csv(DESCRIPTION_TSV, sep="\t").fillna("")
    descriptions: dict[str, dict[str, str]] = {}
    for _, row in df.iterrows():
        code = clean(row.get("NR"))
        first = clean(row.get("Voornaam"))
        last = clean(row.get("Achternaam"))
        if not code or not first or not last:
            continue
        descriptions[normalize(f"{code}-{first}-{last}")] = {
            "title": clean(row.get("Title")),
            "description": clean(row.get("Description")),
            "keywords": clean(row.get("Keywords")),
            "target": clean(row.get("Doelgroep")),
            "context": clean(row.get("Context")),
        }
    return descriptions


def description_entry_for(
    descriptions: dict[str, dict[str, str]],
    code: str,
    first: str,
    last: str,
) -> dict[str, str]:
    return descriptions.get(normalize(f"{code}-{first}-{last}"), {})


def assignment_from(code: str, explicit: str) -> str:
    source = f"{explicit} {code}".upper()
    if "CS" in source or "SENSE" in source or "SENSOR" in source:
        return "circular-sensors"
    return "exoskeletons"


def domain_tags_for(assignment_id: str, target: str, context: str, keywords: str = "") -> list[str]:
    haystack = f"{target} {context} {keywords}".lower()
    tags: set[str] = set()
    if assignment_id == "exoskeletons":
        if any(word in haystack for word in ["medisch", "revalidatie", "artrose", "dropvoet", "zorg", "postpartum", "elderly", "patient", "nursing"]):
            tags.add("healthcare")
        if any(word in haystack for word in ["werk", "haven", "tuin", "kelner", "supermarkt", "bouw", "banden", "worker", "occupational", "manual"]):
            tags.add("workplace")
        if any(word in haystack for word in ["sport", "hardlop", "shin", "knie", "osgood", "mobility", "gait", "cycling", "walking"]):
            tags.add("mobility-sports")
        if not tags:
            tags.add("workplace")
    else:
        if any(word in haystack for word in ["tuin", "bijen", "insect", "wijngaard", "bladnatheid", "bodem", "bird", "wildlife", "biodiversity", "soil", "water"]):
            tags.add("environment")
        if any(word in haystack for word in ["werf", "bouwwerven", "stedelijke", "urban", "traffic", "street", "neighbourhood", "construction"]):
            tags.add("public-space")
        if any(word in haystack for word in ["school", "stem", "student", "citizen", "science", "children", "parents"]):
            tags.add("education-citizen-science")
        if any(word in haystack for word in ["lucht", "fijn stof", "co2", "geluid", "geur", "air", "noise", "emissions"]):
            tags.add("public-space")
        if not tags:
            tags.add("environment")
    return sorted(tags)


def tags_for(assignment_id: str, target: str, context: str) -> list[str]:
    base = ["exoskeleton"] if assignment_id == "exoskeletons" else ["sensor", "circularity"]
    for tag in domain_tags_for(assignment_id, target, context):
        if tag not in base:
            base.append(tag)
    return base


def keyword_tags(keywords: str) -> list[str]:
    tags = []
    for keyword in re.split(r",|;", keywords):
        tag = slugify(keyword.strip())
        if tag and tag != "project" and tag not in tags:
            tags.append(tag)
    return tags[:4]


def child_dirs(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return [item for item in folder.iterdir() if item.is_dir()]


def find_student_folder(section: str, first: str, last: str) -> Path | None:
    folder = CONTENT_ROOT / section
    first_key = normalize(first)
    last_key = normalize(last)
    candidates = child_dirs(folder)
    for candidate in candidates:
        key = normalize(candidate.name)
        if first_key in key and last_key in key:
            return candidate
    return None


def files_for_student(section: str, first: str, last: str) -> list[Path]:
    folder = find_student_folder(section, first, last)
    if not folder:
        return []
    return [item for item in folder.rglob("*") if item.is_file() and item.name != ".DS_Store"]


def choose_pdf(paths: list[Path], prefer: list[str], avoid: list[str] | None = None) -> str:
    avoid = avoid or []
    pdfs = [
        path
        for path in paths
        if path.suffix.lower() == ".pdf" and path.stat().st_size < GITHUB_FILE_LIMIT_BYTES
    ]
    if not pdfs:
        return ""
    ranked = sorted(
        pdfs,
        key=lambda path: (
            not any(term.lower() in path.name.lower() for term in prefer),
            any(term.lower() in path.name.lower() for term in avoid),
            len(path.name),
        ),
    )
    return web_path(ranked[0])


def extract_pdf_text(path: Path, max_pages: int = 4) -> str:
    try:
        reader = PdfReader(str(path))
        page_text = [(page.extract_text() or "") for page in reader.pages[:max_pages]]
        return "\n".join(page_text)
    except Exception:
        return ""


def compact_words(text: str, max_words: int = 18) -> str:
    words = re.findall(r"[\wÀ-ÿ+-]+", text)
    return " ".join(words[:max_words])


def focus_from_text(text: str, fallback: str, student: str) -> str:
    lines = [line.strip(" •\t") for line in text.splitlines()]
    blocked = {
        "bachelorproef",
        "jury",
        "uantwerpen",
        "universiteit antwerpen",
        "university of antwerp",
        "productontwikkeling",
        "portfolio",
        "inhoud",
        "context",
        "probleem",
        "concept",
        "conclusie",
    }
    student_parts = [normalize(part) for part in student.split() if len(part) > 2]
    candidates: list[str] = []
    for line in lines:
        normalized = normalize(line)
        if len(line) < 12 or len(line) > 110:
            continue
        if any(term in normalized for term in blocked):
            continue
        if any(part in normalized for part in student_parts):
            continue
        if re.search(r"@|www|^\d+$|^s0\d+", line, re.I):
            continue
        if len(line.split()) < 3:
            continue
        candidates.append(line)
    return compact_words(candidates[0] if candidates else fallback)


def description_for(
    assignment_id: str,
    student: str,
    target: str,
    context: str,
    presentation_text: str,
    poster_text: str,
    description_entry: dict[str, str] | None = None,
) -> dict[str, str]:
    description_entry = description_entry or {}
    curated_description = description_entry.get("description", "")
    curated_title = description_entry.get("title", "")
    curated_keywords = description_entry.get("keywords", "")
    if curated_description:
        if assignment_id == "exoskeletons":
            nl_kind = "draagbaar ondersteuningssysteem"
            nl_focus = "ergonomie, comfort en betrouwbare ondersteuning"
        else:
            nl_kind = "circulair sensorsysteem"
            nl_focus = "lokale metingen, modulariteit en betekenisvolle data"
        keyword_phrase = f" Trefwoorden: {curated_keywords}." if curated_keywords else ""
        nl_title = f" rond {curated_title}" if curated_title else ""
        return {
            "en": curated_description,
            "nl": (
                f"Dit Bachelorproefproject{nl_title} ontwikkelt een {nl_kind} voor {target}, "
                f"binnen de context {context}. Het project onderzoekt hoe productontwikkeling "
                f"{nl_focus} kan samenbrengen in een helder en toekomstgericht ontwerpvoorstel."
                f"{keyword_phrase}"
            ),
        }

    focus = focus_from_text(f"{presentation_text}\n{poster_text}", f"{target} / {context}", student)
    if assignment_id == "exoskeletons":
        nl_subject = "een draagbaar ondersteuningssysteem"
        en_subject = "a wearable support system"
        nl_angle = "ergonomie, comfort, veiligheid en acceptatie in realistische gebruikssituaties"
        en_angle = "ergonomics, comfort, safety and acceptance in realistic use situations"
    else:
        nl_subject = "een modulair sensorsysteem"
        en_subject = "a modular sensor system"
        nl_angle = "gebruiksgemak, modulariteit, circulariteit en betrouwbare lokale metingen"
        en_angle = "ease of use, modularity, circularity and reliable local measurements"

    return {
        "nl": (
            f"{student} ontwikkelde {nl_subject} voor {target}, binnen de context {context}. "
            f"Het presentatiemateriaal legt de nadruk op {focus}. "
            f"Het project onderzoekt hoe productontwerp {nl_angle} kan samenbrengen in een helder voorstel."
        ),
        "en": (
            f"{student} developed {en_subject} for the target group '{target}' in the context of '{context}'. "
            f"The presentation material highlights {focus}. "
            f"The project explores how product design can connect {en_angle} in a clear concept proposal."
        ),
    }


def render_image_preview(path: Path, project_id: str, index: int) -> str:
    GENERATED_VISUALS.mkdir(parents=True, exist_ok=True)
    output_path = GENERATED_VISUALS / f"{project_id}-{index:02d}.jpg"
    if output_path.exists():
        return web_path(output_path)
    try:
        with Image.open(path) as image:
            image = ImageOps.exif_transpose(image)
            image.thumbnail((1400, 1400), Image.Resampling.LANCZOS)
            if image.mode not in ("RGB", "L"):
                background = Image.new("RGB", image.size, "white")
                if image.mode == "RGBA":
                    background.paste(image, mask=image.getchannel("A"))
                else:
                    background.paste(image)
                image = background
            else:
                image = image.convert("RGB")
            image.save(output_path, "JPEG", quality=78, optimize=True, progressive=True)
            return web_path(output_path)
    except Exception:
        return ""


def render_pdf_preview(path: Path, project_id: str, index: int, output_dir: Path = GENERATED_VISUALS) -> str:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_stem = f"{project_id}-{index:02d}"
    output_path = output_dir / f"{output_stem}.png"
    if output_path.exists():
        return web_path(output_path)

    temporary_dir = output_dir / "_tmp"
    temporary_dir.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["qlmanage", "-t", "-s", "1200", "-o", str(temporary_dir), str(path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        generated = temporary_dir / f"{path.name}.png"
        if generated.exists():
            generated.replace(output_path)
            return web_path(output_path)
    except Exception:
        return ""
    return ""


def choose_visuals(paths: list[Path], project_id: str) -> list[str]:
    image_exts = {".jpg", ".jpeg", ".png", ".webp"}
    images = [path for path in paths if path.suffix.lower() in image_exts]
    visuals = []
    if not PUBLIC_ASSETS_ONLY:
        visuals = [web_path(path) for path in sorted(images, key=lambda path: path.name.lower())[:MAX_INSTAGRAM_VISUALS]]
    else:
        for image in sorted(images, key=lambda path: path.name.lower()):
            preview = render_image_preview(image, project_id, len(visuals) + 1)
            if preview:
                visuals.append(preview)
            if len(visuals) >= MAX_INSTAGRAM_VISUALS:
                return visuals

    pdfs = [path for path in paths if path.suffix.lower() == ".pdf"]
    for pdf in sorted(pdfs, key=lambda path: path.name.lower()):
        preview = render_pdf_preview(pdf, project_id, len(visuals) + 1)
        if preview:
            visuals.append(preview)
        if len(visuals) >= MAX_INSTAGRAM_VISUALS:
            break
    return visuals


def build_projects() -> list[dict]:
    df = pd.read_excel(STUDENT_LIST, sheet_name="LIJST + BEGELEIDER")
    descriptions = load_student_descriptions()
    projects: list[dict] = []
    seen: set[str] = set()

    for _, row in df.iterrows():
        code = clean(row.get("Unnamed: 1"))
        last = clean(row.get("Unnamed: 2"))
        first = clean(row.get("Unnamed: 3"))
        target = clean(row.get("doelgroep"))
        context = clean(row.get("context"))
        explicit = clean(row.get("EX/CS"))

        if not code or not first or not last or not target or not context:
            continue
        if not re.search(r"(EX|CS|SENSE|SENSOR)", code.upper()):
            continue

        assignment_id = assignment_from(code, explicit)
        student = f"{first} {last}"
        project_id = slugify(f"{code}-{student}")
        if project_id in seen:
            continue
        seen.add(project_id)
        description_entry = description_entry_for(descriptions, code, first, last)

        fiche_files = files_for_student("Fiche", first, last)
        presentation_files = files_for_student("Eindpresentatie", first, last)
        instagram_files = files_for_student("Instagram", first, last)
        poster = choose_pdf(fiche_files, ["fiche"])
        presentation = choose_pdf(presentation_files, ["jury"], ["verslag", "fiche"])
        images = choose_visuals(instagram_files, project_id)
        poster_preview = ""
        if poster:
            poster_preview = render_pdf_preview(ROOT / unquote(poster), project_id, 0, GENERATED_POSTERS)
        if not images and poster_preview:
            images.append(poster_preview)
        poster_text = extract_pdf_text(ROOT / unquote(poster)) if poster else ""
        presentation_text = extract_pdf_text(ROOT / unquote(presentation)) if presentation else ""
        public_poster = "" if PUBLIC_ASSETS_ONLY else poster
        public_presentation = "" if PUBLIC_ASSETS_ONLY else presentation

        assignment_title = "Exoskeleton" if assignment_id == "exoskeletons" else "Circular Sensor"
        nl_assignment_title = "Exoskelet" if assignment_id == "exoskeletons" else "Circulaire Sensor"
        title_en = description_entry.get("title") or f"{assignment_title} for {target}"
        title_nl = description_entry.get("title") or f"{nl_assignment_title} voor {target}"
        filter_tags = domain_tags_for(
            assignment_id,
            target,
            context,
            " ".join([
                description_entry.get("title", ""),
                description_entry.get("description", ""),
                description_entry.get("keywords", ""),
            ]),
        )
        tags = tags_for(assignment_id, target, context)
        for tag in keyword_tags(description_entry.get("keywords", "")):
            if tag not in tags:
                tags.append(tag)

        projects.append(
            {
                "id": project_id,
                "code": code,
                "assignmentId": assignment_id,
                "student": student,
                "featured": len(projects) < 6,
                "title": {"en": title_en, "nl": title_nl},
                "summary": {
                    **description_for(assignment_id, student, target, context, presentation_text, poster_text, description_entry),
                },
                "context": {"en": context, "nl": context},
                "targetGroup": {"en": target, "nl": target},
                "tags": tags,
                "filterTags": filter_tags,
                "assets": {
                    "thumbnail": poster_preview or (images[0] if images else ""),
                    "poster": public_poster,
                    "posterPreview": poster_preview,
                    "presentation": public_presentation,
                    "visuals": images,
                },
            }
        )
    return projects


def write_outputs(projects: list[dict]) -> None:
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JS.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "courses": [
            {
                "id": "bachelor-proef",
                "name": "Bachelor Proef",
                "year": "2025-2026",
                "description": {
                    "en": "Individual Product Development projects exploring future-facing design challenges through research, concept development, prototyping, and communication.",
                    "nl": "Individuele projecten Productontwikkeling waarin studenten toekomstgerichte ontwerpuitdagingen verkennen via onderzoek, conceptontwikkeling, prototyping en communicatie.",
                },
                "objectives": {
                    "en": [
                        "Logical design reasoning",
                        "Research and verification",
                        "Integrated product design",
                        "Professional communication",
                    ],
                    "nl": [
                        "Logische ontwerpvaardigheden",
                        "Onderzoeken en verifiëren",
                        "Integraal productontwerp",
                        "Professioneel communiceren",
                    ],
                },
                "sourceDocuments": [] if PUBLIC_ASSETS_ONLY else [
                    {
                        "label": {
                            "en": "Assignment brief",
                            "nl": "Opdrachtomschrijving",
                        },
                        "path": "Content/2025-2026/Bachelorproef/UA_PO_Bachelorproef_25-26_Opdracht_v1-met%20structuur.docx",
                    },
                    {
                        "label": {
                            "en": "Course presentation",
                            "nl": "Cursuspresentatie",
                        },
                        "path": "Content/2025-2026/Bachelorproef/UA_PO_Bachelorproef_25-26_Presentatie_draft_Jsd.pdf",
                    },
                ],
            }
        ],
        "years": [
            {
                "id": "2025-2026",
                "label": "2025-2026",
                "status": {"en": "Current Bachelor Proef showcase", "nl": "Huidige bachelorproefshowcase"},
            },
            {
                "id": "2024-2025",
                "label": "2024-2025",
                "status": {"en": "Archive placeholder", "nl": "Archiefplaceholder"},
            },
        ],
        "assignments": [
            {
                "id": "exoskeletons",
                "course": "Bachelor Proef",
                "year": "2025-2026",
                "color": "#EA2C38",
                "title": {"en": "Exoskeletons", "nl": "Exoskeletten"},
                "description": {
                    "en": "Wearable support systems that explore how future products can extend, protect, or assist the human body.",
                    "nl": "Draagbare ondersteuningssystemen die onderzoeken hoe toekomstige producten het menselijk lichaam kunnen versterken, beschermen of ondersteunen.",
                },
                "longDescription": {
                    "en": "The exoskeleton assignment asks students to design future product concepts around bodily support, movement, work, care, rehabilitation, and performance. These projects are especially visual and suitable for collaboration conversations with companies and research partners.",
                    "nl": "De opdracht rond exoskeletten vraagt studenten om toekomstgerichte productconcepten te ontwerpen rond lichamelijke ondersteuning, beweging, werk, zorg, revalidatie en prestaties. Deze projecten zijn visueel sterk en geschikt voor gesprekken met bedrijven en onderzoekspartners.",
                },
                "brief": {
                    "partners": "Huskk, To Walk Again",
                    "challenge": {
                        "en": "Design a compact, comfortable, safe and intuitive exoskeleton or wearable support system that assists people with daily tasks at home or in work contexts.",
                        "nl": "Ontwerp een compact, comfortabel, veilig en intuïtief exoskelet of draagbaar ondersteuningssysteem dat mensen helpt bij dagelijkse taken thuis of in een werkcontext.",
                    },
                    "background": {
                        "en": "Many people experience physical strain while lifting, carrying, bending, climbing stairs, standing for long periods or repeating movements. Existing solutions are often too bulky, expensive, complex, visible or poorly adapted to real daily situations.",
                        "nl": "Veel mensen ervaren fysieke belasting bij tillen, dragen, bukken, traplopen, lang rechtstaan of repetitieve bewegingen. Bestaande oplossingen zijn vaak te log, duur, complex, zichtbaar of onvoldoende afgestemd op realistische dagelijkse situaties.",
                    },
                    "goals": {
                        "en": [
                            "Make support easy to put on, adjust and understand",
                            "Respect ergonomics, comfort and different body types",
                            "Build in safe, reliable and fail-safe behaviour",
                            "Avoid a stigmatizing or overly robotic appearance",
                            "Use durable, repairable and scalable product architecture",
                        ],
                        "nl": [
                            "Ondersteuning eenvoudig aantrekbaar, afstelbaar en begrijpbaar maken",
                            "Ergonomie, comfort en verschillende lichaamstypes respecteren",
                            "Veilig, betrouwbaar en fail-safe gedrag voorzien",
                            "Een stigmatiserende of te robotachtige uitstraling vermijden",
                            "Werken met een duurzame, herstelbare en schaalbare productarchitectuur",
                        ],
                    },
                    "analysisFocus": {
                        "en": [
                            "Context analysis of realistic environments and spatial constraints",
                            "User analysis including activity flows and ergonomic data",
                            "Desk review of passive, active and hybrid support principles",
                        ],
                        "nl": [
                            "Contextanalyse van realistische omgevingen en ruimtelijke randvoorwaarden",
                            "Gebruikersanalyse met activiteitenflows en ergonomische data",
                            "Desk review van passieve, actieve en hybride ondersteuningsprincipes",
                        ],
                    },
                },
            },
            {
                "id": "circular-sensors",
                "course": "Bachelor Proef",
                "year": "2025-2026",
                "color": "#82A1AD",
                "title": {"en": "Circular Sensors", "nl": "Circulaire Sensoren"},
                "description": {
                    "en": "Sensor-driven product concepts that combine data, circularity, responsible material choices, and sustainable use contexts.",
                    "nl": "Sensorgedreven productconcepten die data, circulariteit, verantwoorde materiaalkeuzes en duurzame gebruikscontexten combineren.",
                },
                "longDescription": {
                    "en": "The circular sensors assignment focuses on smart product-service ideas that treat sensing as part of a circular system: maintainable, repairable, meaningful, and careful with materials and data.",
                    "nl": "De opdracht rond circulaire sensoren focust op slimme product-dienstconcepten waarin sensoren deel zijn van een circulair systeem: onderhoudbaar, herstelbaar, betekenisvol en zorgvuldig met materialen en data.",
                },
                "brief": {
                    "partners": "imec, Superellipse",
                    "challenge": {
                        "en": "Design a modular, circular and user-friendly environmental sensor system for citizen science and local environmental measurements.",
                        "nl": "Ontwerp een modulair, circulair en gebruiksvriendelijk sensorsysteem voor burgerwetenschap en lokale omgevingsmetingen.",
                    },
                    "background": {
                        "en": "Pollution and exposure vary strongly by street, school, home type, ventilation and proximity to traffic. Local measurements can reveal hotspots and peaks, but citizen-science systems must also reach groups that are usually harder to involve.",
                        "nl": "Vervuiling en blootstelling verschillen sterk per straat, school, woningtype, ventilatie en nabijheid van verkeer. Lokale metingen kunnen hotspots en pieken zichtbaar maken, maar citizen-science systemen moeten ook moeilijker bereikbare doelgroepen betrekken.",
                    },
                    "goals": {
                        "en": [
                            "Support different measurement domains such as air, sound, soil or water",
                            "Make installation, maintenance and interpretation accessible to non-technical users",
                            "Enable repair, upgrade and reconfiguration without full replacement",
                            "Fit aesthetically into gardens, facades, streets or interiors",
                            "Scale to larger measurement campaigns and return/reuse logistics",
                        ],
                        "nl": [
                            "Verschillende meetdomeinen ondersteunen, zoals lucht, geluid, bodem of water",
                            "Installatie, onderhoud en interpretatie toegankelijk maken voor niet-technische gebruikers",
                            "Herstel, upgrade en herconfiguratie mogelijk maken zonder volledige vervanging",
                            "Esthetisch passen in tuinen, gevels, straten of interieurs",
                            "Schaalbaar zijn voor grotere meetcampagnes en logistiek rond terugname/hergebruik",
                        ],
                    },
                    "analysisFocus": {
                        "en": [
                            "Context analysis of realistic homes, shared spaces and local environments",
                            "Use analysis for citizens, researchers, installation, diagnosis, repair and upgrade",
                            "Desk review of existing citizen-science and IoT sensor kits",
                        ],
                        "nl": [
                            "Contextanalyse van realistische woningen, gedeelde ruimtes en lokale omgevingen",
                            "Gebruiksanalyse voor burgers, onderzoekers, installatie, diagnose, repair en upgrade",
                            "Desk review van bestaande citizen-science en IoT-sensorkits",
                        ],
                    },
                },
            },
        ],
        "projects": projects,
    }

    OUTPUT_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    OUTPUT_JS.write_text(
        "export const content = "
        + json.dumps(data, indent=2, ensure_ascii=False)
        + ";\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    generated_projects = build_projects()
    write_outputs(generated_projects)
    print(f"Generated {len(generated_projects)} projects")
