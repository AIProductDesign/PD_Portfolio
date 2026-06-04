# Stijlguide Portfolio-website Productontwikkeling

**Voor:** Opleiding Productontwikkeling & Research Group Product Development  
**Context:** Faculteit Ontwerpwetenschappen / Faculty of Design Sciences, Universiteit Antwerpen  
**Gebruik:** Dit document dient als briefing voor Codex of een andere AI/developer om een portfolio-website te genereren in de juiste stijl.  
**Versie:** 1.0  
**Datum:** 2026-06-04

---

## 1. Doel van deze stijlguide

Deze stijlguide beschrijft hoe een portfolio-website voor **Productontwikkeling** aan de **Universiteit Antwerpen** visueel, inhoudelijk en technisch moet worden opgezet.

De website moet:

- herkenbaar aansluiten bij de officiële huisstijl van de Universiteit Antwerpen;
- duidelijk ingebed zijn in de **Faculteit Ontwerpwetenschappen / Faculty of Design Sciences**;
- de identiteit van **Productontwikkeling** zichtbaar maken zonder een los merk te creëren;
- bruikbaar zijn voor onderwijsportfolio’s, onderzoeksgroepcommunicatie, projectpagina’s, student work, demonstratoren en samenwerkingen;
- geschikt zijn voor verdere implementatie met Codex, bijvoorbeeld in HTML/CSS, React, Next.js, Astro, Vite of een statische websitegenerator.

De algemene UA-huisstijlgids blijft leidend:

```text
https://www.uantwerpen.be/nl/projecten/huisstijlgids/
```

---

## 2. Belangrijkste merkregel

Productontwikkeling is **geen autonoom merk** buiten de Universiteit Antwerpen.

De portfolio-website moet daarom worden opgebouwd als:

```text
Universiteit Antwerpen
└── Faculteit Ontwerpwetenschappen / Faculty of Design Sciences
    └── Productontwikkeling / Product Development
        ├── Opleiding
        └── Onderzoeksgroep
```

### Implicatie voor de website

Gebruik:

- de officiële UA-logo’s;
- de officiële faculteitskleur van Ontwerpwetenschappen;
- een tekstuele aanduiding van Productontwikkeling;
- geen zelfontworpen opleidingslogo;
- geen alternatieve merkidentiteit die losstaat van UA.

De visuele identiteit moet aanvoelen als:

> **UAntwerpen als institutionele basis + Ontwerpwetenschappen als visuele context + Productontwikkeling als inhoudelijke ontwerpstem.**

---

## 3. Lokale bestanden in dezelfde folder

Plaats bij voorkeur de volgende bestanden in dezelfde hoofdmap als deze stijlguide of in een duidelijke submap zoals `assets/` of `templates/`.

### 3.1 Aanbevolen folderstructuur

```text
portfolio-website/
├── productontwikkeling_portfolio_styleguide.md
├── README.md
├── assets/
│   ├── logos/
│   │   ├── ua-logo-primary.svg
│   │   ├── ua-logo-negative.svg
│   │   ├── ua-logo-primary.png
│   │   ├── faculty-design-sciences-logo.svg
│   │   └── research-group-product-development-logo.svg
│   ├── images/
│   │   ├── hero/
│   │   ├── projects/
│   │   ├── students/
│   │   └── research/
│   └── icons/
├── templates/
│   ├── ua-powerpoint-template.pptx
│   ├── faculty-design-sciences-powerpoint-template.pptx
│   ├── ua-word-template.docx
│   └── faculty-design-sciences-word-template.docx
├── src/
│   ├── components/
│   ├── pages/
│   ├── styles/
│   └── data/
└── public/
```

### 3.2 Bestanden waar Codex rekening mee moet houden

Codex moet lokale bestanden gebruiken wanneer ze aanwezig zijn. De exacte bestandsnamen mogen aangepast worden, maar gebruik bij voorkeur deze conventie.

| Type | Voorkeursnaam | Gebruik |
|---|---|---|
| UA-logo primair | `assets/logos/ua-logo-primary.svg` | Header, footer, officiële context |
| UA-logo negatief | `assets/logos/ua-logo-negative.svg` | Donkere of fotografische achtergrond |
| Faculteitslogo | `assets/logos/faculty-design-sciences-logo.svg` | Indien beschikbaar en toegestaan volgens UA-richtlijnen |
| Onderzoeksgroeplogo | `assets/logos/research-group-product-development-logo.svg` | Enkel voor officiële onderzoeksgroepcommunicatie |
| PowerPoint-template UA | `templates/ua-powerpoint-template.pptx` | Referentie voor slide-layout, kleurgebruik en presentatiehiërarchie |
| PowerPoint-template faculteit | `templates/faculty-design-sciences-powerpoint-template.pptx` | Belangrijkste visuele referentie voor web-layout |
| Word-template UA | `templates/ua-word-template.docx` | Referentie voor typografie, titels, tekststructuur |
| Word-template faculteit | `templates/faculty-design-sciences-word-template.docx` | Referentie voor facultaire documenten en kleurgebruik |

### 3.3 Regel voor ontbrekende bestanden

Wanneer een logo of template niet aanwezig is, mag Codex:

- geen fictief UA-logo genereren;
- geen alternatief logo ontwerpen;
- een tekstuele placeholder gebruiken, bijvoorbeeld `[UA logo]`;
- in de code een duidelijke `TODO` voorzien;
- visueel werken met kleur, typografie, witruimte en structuur totdat de officiële assets toegevoegd worden.

Voorbeeld:

```html
<!-- TODO: Replace with official UA logo from assets/logos/ua-logo-primary.svg -->
<div class="logo-placeholder">Universiteit Antwerpen</div>
```

---

## 4. Merknamen en tekstuele aanduidingen

Gebruik consistente naamgeving.

| Nederlands | Engels |
|---|---|
| Universiteit Antwerpen | University of Antwerp |
| Faculteit Ontwerpwetenschappen | Faculty of Design Sciences |
| Productontwikkeling | Product Development |
| Opleiding Productontwikkeling | Product Development programme |
| Onderzoeksgroep Productontwikkeling | Product Development Research Group |
| Research Group Product Development | Research Group Product Development |

### Aanbevolen hoofdtitel website

Voor een Nederlandstalige site:

```text
Productontwikkeling
Faculteit Ontwerpwetenschappen — Universiteit Antwerpen
```

Voor een Engelstalige site:

```text
Product Development
Faculty of Design Sciences — University of Antwerp
```

Voor een tweetalige of internationale portfolio-site:

```text
Product Development / Productontwikkeling
Faculty of Design Sciences — University of Antwerp
```

---

## 5. Visuele positionering

De portfolio-website moet visueel de volgende kwaliteiten uitstralen:

- academisch betrouwbaar;
- ontwerpgericht;
- mensgericht;
- technologisch onderbouwd;
- duurzaam en circulair;
- experimenteel maar professioneel;
- helder, ruimtelijk en niet overvol;
- gericht op prototypes, demonstratoren, onderzoek en maatschappelijke impact.

### Kernwoorden

```text
Human-centered
Design-driven
Research-based
Circular
Smart products
Prototyping
Product-service systems
Materiality
Technology
Interaction
Future-oriented
```

---

## 6. Kleuren

### 6.1 Officiële UA-basiskleuren

Gebruik deze kleuren als vaste design tokens.

| Naam | HEX | RGB | Gebruik |
|---|---:|---:|---|
| UA Red | `#EA2C38` | 234, 44, 56 | UA-herkenning, call-to-action, kleine accenten |
| UA Blue | `#002E65` | 0, 46, 101 | Titels, navigatie, footer, institutionele basis |

### 6.2 Faculteitskleur Ontwerpwetenschappen

| Naam | HEX | RGB | Gebruik |
|---|---:|---:|---|
| Design Sciences | `#82A1AD` | 130, 161, 173 | Hoofdaccent Productontwikkeling binnen faculteitscontext |
| Design Sciences Pastel | `#C8D9D8` | 200, 217, 216 | Zachte achtergrondvlakken, cards, labels |

### 6.3 Neutrale ondersteunende kleuren

Deze kleuren mogen worden gebruikt als praktische webkleuren.

| Naam | HEX | Gebruik |
|---|---:|---|
| White | `#FFFFFF` | Hoofdachtergrond |
| Off White | `#F7F8F8` | Sectieachtergrond |
| Light Grey | `#E8ECEE` | Borders, subtiele lijnen |
| Medium Grey | `#687782` | Metadata, captions, secundaire tekst |
| Dark Grey | `#1F2933` | Bodytekst |
| Near Black | `#111827` | Sterke tekstcontrast |

### 6.4 CSS design tokens

Gebruik bij voorkeur CSS variables.

```css
:root {
  --ua-red: #EA2C38;
  --ua-blue: #002E65;

  --fds-bluegrey: #82A1AD;
  --fds-bluegrey-pastel: #C8D9D8;

  --color-white: #FFFFFF;
  --color-offwhite: #F7F8F8;
  --color-lightgrey: #E8ECEE;
  --color-mediumgrey: #687782;
  --color-darkgrey: #1F2933;
  --color-nearblack: #111827;

  --color-background: var(--color-white);
  --color-background-soft: var(--color-offwhite);
  --color-text: var(--color-darkgrey);
  --color-heading: var(--ua-blue);
  --color-accent: var(--fds-bluegrey);
  --color-accent-soft: var(--fds-bluegrey-pastel);
  --color-cta: var(--ua-red);

  --border-radius-sm: 0.5rem;
  --border-radius-md: 1rem;
  --border-radius-lg: 1.5rem;

  --shadow-soft: 0 12px 32px rgba(0, 46, 101, 0.08);
  --shadow-card: 0 8px 24px rgba(0, 46, 101, 0.10);

  --max-width-content: 1180px;
  --max-width-narrow: 760px;
}
```

### 6.5 Kleurgebruik op de website

Gebruik:

- wit als dominante achtergrond;
- UA Blue voor headers, navigatie, footer en titels;
- Design Sciences Bluegrey voor accenten, labels, lijnen en visuele herkenning;
- Design Sciences Pastel voor rustige achtergrondvlakken en projectcards;
- UA Red spaarzaam voor primaire acties, highlights of belangrijke links.

Vermijd:

- willekeurige alternatieve blauwtinten;
- felgekleurde gradients die niet bij UA passen;
- rode vlakken als dominante achtergrond;
- tekst in pastelkleuren met onvoldoende contrast.

---

## 7. Typografie

De officiële UA-huisstijl gebruikt specifieke fonts, maar voor een webimplementatie moeten officiële fonts enkel gebruikt worden wanneer ze correct beschikbaar en gelicentieerd zijn.

### 7.1 Praktische webregel

Codex mag geen fontbestanden verzinnen of embedden. Gebruik veilige fallback fonts tenzij de officiële UA-fonts lokaal of via een correcte bron beschikbaar zijn.

Aanbevolen font stack:

```css
:root {
  --font-sans: Calibri, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-display: Calibri, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-mono: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, monospace;
}
```

### 7.2 Typografische hiërarchie

```css
body {
  font-family: var(--font-sans);
  font-size: 16px;
  line-height: 1.6;
  color: var(--color-text);
  background: var(--color-background);
}

h1, h2, h3, h4 {
  font-family: var(--font-display);
  color: var(--color-heading);
  line-height: 1.12;
  letter-spacing: -0.015em;
}

h1 {
  font-size: clamp(2.4rem, 6vw, 5.6rem);
  font-weight: 700;
}

h2 {
  font-size: clamp(1.8rem, 4vw, 3.2rem);
  font-weight: 700;
}

h3 {
  font-size: clamp(1.25rem, 2vw, 1.75rem);
  font-weight: 700;
}

.lead {
  font-size: clamp(1.15rem, 2vw, 1.45rem);
  line-height: 1.55;
  color: var(--color-darkgrey);
}

.meta,
.caption {
  font-size: 0.875rem;
  color: var(--color-mediumgrey);
}
```

### 7.3 Tekststijl

Schrijf helder, actief en concreet.

Goed:

```text
We design and test prototypes that connect human needs, technological possibilities and sustainable product systems.
```

Minder goed:

```text
We deliver innovative future-proof solutions through cutting-edge disruption.
```

---

## 8. Logo- en headergebruik

### 8.1 Headerstructuur

De header moet institutioneel duidelijk zijn, maar de portfolio-inhoud niet overheersen.

Aanbevolen desktop-header:

```text
[UA logo]   Product Development / Productontwikkeling
            Faculty of Design Sciences

Navigation: Work | Research | Education | People | Partners | Contact
```

Aanbevolen mobiele header:

```text
[UA logo]
Product Development
[menu]
```

### 8.2 Logo-regels

Codex moet:

- officiële logo-assets gebruiken wanneer ze aanwezig zijn;
- de aspect ratio van logo’s behouden;
- voldoende vrije ruimte rond het logo respecteren;
- het logo niet vervormen, recoloren of reconstrueren;
- geen losstaande “U” gebruiken tenzij dat expliciet als officieel social-media-asset beschikbaar is;
- bij ontbrekend logo een tekstuele fallback tonen.

Voorbeeld:

```html
<header class="site-header">
  <a class="brand" href="/" aria-label="Product Development, University of Antwerp">
    <img src="/assets/logos/ua-logo-primary.svg" alt="Universiteit Antwerpen" class="brand-logo" />
    <span class="brand-context">
      <strong>Product Development</strong>
      <span>Faculty of Design Sciences</span>
    </span>
  </a>
</header>
```

```css
.brand {
  display: inline-flex;
  align-items: center;
  gap: 1rem;
  color: var(--ua-blue);
  text-decoration: none;
}

.brand-logo {
  height: 44px;
  width: auto;
}

.brand-context {
  display: flex;
  flex-direction: column;
  line-height: 1.15;
}

.brand-context span {
  color: var(--color-mediumgrey);
  font-size: 0.9rem;
}
```

---

## 9. Beeldtaal

De website moet echte ontwerp- en onderzoekssituaties tonen.

### 9.1 Voorkeursbeelden

Gebruik beelden van:

- prototypes;
- demonstratoren;
- studentenwerk;
- werkplaatsen en studio’s;
- labs en testopstellingen;
- interactie tussen mens, product en context;
- materiaalonderzoek;
- circulaire producten;
- herstel, demontage, hergebruik en levensduurverlenging;
- slimme producten, sensoren, elektronica en interfaces;
- co-creatie met bedrijven, burgers, zorg, industrie of publieke organisaties;
- presentaties, design reviews, jurymomenten en expo’s.

### 9.2 Vermijd

Vermijd:

- generieke stockfoto’s;
- abstracte AI- of innovatiebeelden zonder context;
- overdreven futuristische renders;
- decoratieve beelden zonder inhoudelijke functie;
- rommelige werkplaatsfoto’s zonder visuele focus;
- zware kleurfilters die de UA-huisstijl verstoren.

### 9.3 Beeldbehandeling

Gebruik:

- afgeronde hoeken;
- subtiele borders;
- ruime witruimte;
- rustige captions;
- eventueel eenvoudige technische overlays zoals lijnen, labels of exploded-view-fragmenten.

Voorbeeld CSS:

```css
.image-card {
  border-radius: var(--border-radius-lg);
  overflow: hidden;
  background: var(--color-background-soft);
  box-shadow: var(--shadow-soft);
}

.image-card img {
  display: block;
  width: 100%;
  height: auto;
  object-fit: cover;
}

.image-card figcaption {
  padding: 0.85rem 1rem 1rem;
  font-size: 0.9rem;
  color: var(--color-mediumgrey);
}
```

---

## 10. Layoutprincipes

### 10.1 Algemene layout

Gebruik een heldere, modulaire en rustige layout.

Basisprincipes:

- veel witruimte;
- duidelijke gridstructuur;
- korte contentblokken;
- sterke hero-sectie;
- visuele kaarten voor projecten;
- consistente sectie-indeling;
- duidelijke call-to-actions;
- voldoende contrast;
- responsive vanaf mobiel tot groot scherm.

### 10.2 Grid

```css
.container {
  width: min(100% - 2rem, var(--max-width-content));
  margin-inline: auto;
}

.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: clamp(1.5rem, 4vw, 4rem);
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
}

@media (max-width: 860px) {
  .grid-2,
  .grid-3 {
    grid-template-columns: 1fr;
  }
}
```

### 10.3 Secties

Elke pagina gebruikt bij voorkeur deze opbouw:

```text
Header
Hero
Intro / positioning
Featured projects
Research themes
Education / student work
Partners / collaborations
People or contact
Footer
```

---

## 11. Componenten

### 11.1 Hero

De hero moet onmiddellijk duidelijk maken wat Productontwikkeling doet.

Aanbevolen inhoud:

```text
Product Development / Productontwikkeling
Design-driven research and education for human-centered, circular and technology-enabled products.
Faculty of Design Sciences — University of Antwerp
```

Voorbeeld HTML:

```html
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">Faculty of Design Sciences — University of Antwerp</p>
      <h1>Designing responsible product futures.</h1>
      <p class="lead">
        Product Development connects human needs, technological possibilities and circular design strategies through education, research and demonstrators.
      </p>
      <div class="hero-actions">
        <a class="button button-primary" href="#projects">Explore projects</a>
        <a class="button button-secondary" href="#research">Research themes</a>
      </div>
    </div>
    <figure class="hero-image image-card">
      <img src="/assets/images/hero/product-development-studio.jpg" alt="Students and researchers working on product prototypes" />
    </figure>
  </div>
</section>
```

Voorbeeld CSS:

```css
.hero {
  padding: clamp(4rem, 10vw, 8rem) 0;
  background:
    linear-gradient(120deg, var(--color-white) 0%, var(--color-white) 58%, var(--fds-bluegrey-pastel) 58%, var(--fds-bluegrey-pastel) 100%);
}

.hero-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(320px, 0.95fr);
  gap: clamp(2rem, 5vw, 5rem);
  align-items: center;
}

.eyebrow {
  color: var(--fds-bluegrey);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.8rem;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  margin-top: 2rem;
}
```

### 11.2 Buttons

```css
.button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  padding: 0.8rem 1.2rem;
  font-weight: 700;
  text-decoration: none;
  transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
}

.button:hover {
  transform: translateY(-1px);
}

.button-primary {
  background: var(--ua-red);
  color: var(--color-white);
  box-shadow: var(--shadow-card);
}

.button-secondary {
  background: var(--color-white);
  color: var(--ua-blue);
  border: 1px solid var(--color-lightgrey);
}
```

### 11.3 Projectcards

Projectcards zijn de kern van de portfolio-website.

Elke projectcard bevat idealiter:

- titel;
- korte samenvatting;
- beeld;
- tags;
- jaar;
- type: `Student Work`, `Research`, `Collaboration`, `Demo`, `Thesis`;
- betrokken partners;
- link naar detailpagina.

Voorbeeld data-object:

```js
const projects = [
  {
    title: "Circular Sensor Kit",
    type: "Research / Student Work",
    year: "2025–2026",
    summary: "A modular sensor platform exploring repairability, reconfiguration and circular electronics for citizen science.",
    tags: ["Circularity", "Sensors", "Smart Products", "Citizen Science"],
    image: "/assets/images/projects/circular-sensor-kit.jpg",
    partners: ["imec", "University of Antwerp"],
    href: "/projects/circular-sensor-kit"
  }
];
```

Voorbeeld HTML:

```html
<article class="project-card">
  <a href="/projects/circular-sensor-kit" class="project-card-image">
    <img src="/assets/images/projects/circular-sensor-kit.jpg" alt="Circular sensor kit prototype" />
  </a>
  <div class="project-card-content">
    <p class="project-meta">Research / Student Work · 2025–2026</p>
    <h3><a href="/projects/circular-sensor-kit">Circular Sensor Kit</a></h3>
    <p>A modular sensor platform exploring repairability, reconfiguration and circular electronics for citizen science.</p>
    <ul class="tag-list">
      <li>Circularity</li>
      <li>Sensors</li>
      <li>Smart Products</li>
    </ul>
  </div>
</article>
```

Voorbeeld CSS:

```css
.project-card {
  display: flex;
  flex-direction: column;
  background: var(--color-white);
  border: 1px solid var(--color-lightgrey);
  border-radius: var(--border-radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-soft);
}

.project-card-image img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
}

.project-card-content {
  padding: 1.25rem;
}

.project-card h3 a {
  color: var(--ua-blue);
  text-decoration: none;
}

.project-meta {
  color: var(--fds-bluegrey);
  font-weight: 700;
  font-size: 0.85rem;
}

.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
  padding: 0;
  margin: 1rem 0 0;
  list-style: none;
}

.tag-list li {
  border-radius: 999px;
  background: var(--fds-bluegrey-pastel);
  color: var(--ua-blue);
  padding: 0.3rem 0.65rem;
  font-size: 0.8rem;
  font-weight: 700;
}
```

### 11.4 Research theme cards

Gebruik research theme cards voor bredere thema’s.

Aanbevolen thema’s:

```text
Circular Product Design
Smart Products & Interaction
Human-Centered Design
Product-Service Systems
Digital & Computational Design
Repair, Reuse & Lifecycle Extension
Design Research Methods
Prototyping & Demonstrators
```

Voorbeeld:

```html
<section class="themes section-soft" id="research">
  <div class="container">
    <p class="eyebrow">Research themes</p>
    <h2>Design research for responsible product futures.</h2>
    <div class="theme-grid grid-3">
      <article class="theme-card">
        <h3>Circular Product Design</h3>
        <p>Design strategies for repairability, upgradeability, reuse and longer product lifetimes.</p>
      </article>
      <article class="theme-card">
        <h3>Smart Products & Interaction</h3>
        <p>Human-centered interfaces, sensors, connected products and meaningful interaction.</p>
      </article>
      <article class="theme-card">
        <h3>Product-Service Systems</h3>
        <p>New value models that shift product development from ownership to access, use and impact.</p>
      </article>
    </div>
  </div>
</section>
```

---

## 12. Informatiearchitectuur website

### 12.1 Aanbevolen navigatie

Voor een portfolio-website:

```text
Home
Projects
Research
Education
People
Partners
Contact
```

Voor een compactere website:

```text
Work
Research
Education
About
Contact
```

### 12.2 Aanbevolen pagina’s

#### Home

Doel: positionering en toegang tot de belangrijkste projecten.

Inhoud:

- hero;
- korte positionering;
- featured projects;
- research themes;
- onderwijs en student work;
- partners;
- call-to-action.

#### Projects / Portfolio

Doel: overzicht van projecten.

Filters:

- jaar;
- type;
- thema;
- opleiding / onderzoek;
- partner;
- bachelor / master / PhD / research.

#### Projectdetailpagina

Elke projectpagina bevat:

```text
Titel
Type project
Jaar
Team / studenten / onderzoekers
Partners
Probleemstelling
Ontwerpvraag / onderzoeksvraag
Proces
Prototype / demonstrator
Resultaten
Impact
Beelden
Publicaties of links
Contactpersoon
```

#### Research

Doel: onderzoeksgroep voorstellen.

Inhoud:

- missie;
- thema’s;
- methodes;
- lopende projecten;
- publicaties of output;
- infrastructuur;
- samenwerking.

#### Education

Doel: opleiding Productontwikkeling tonen.

Inhoud:

- bachelor/master-context;
- studio-based learning;
- student projects;
- skills;
- samenwerking met werkveld;
- eindwerken en portfolio’s.

#### People

Doel: team en betrokken onderzoekers/docenten tonen.

Inhoud:

- professors;
- researchers;
- PhD researchers;
- teaching team;
- associated labs;
- contact.

#### Partners

Doel: ecosysteem tonen.

Inhoud:

- bedrijven;
- onderzoekscentra;
- publieke partners;
- internationale partners;
- projectmatige samenwerkingen.

---

## 13. Contentmodel voor projecten

Codex kan de website genereren met statische data in JSON, Markdown of MDX.

### 13.1 Project frontmatter

Gebruik dit model voor projectpagina’s.

```yaml
---
title: "Circular Sensor Kit"
subtitle: "Modular electronics for citizen science and circular product design"
type: "Research / Student Work"
year: "2025-2026"
themes:
  - Circular Product Design
  - Smart Products
  - Citizen Science
  - Modular Electronics
partners:
  - University of Antwerp
  - imec
programme: "Product Development"
faculty: "Faculty of Design Sciences"
coverImage: "/assets/images/projects/circular-sensor-kit/cover.jpg"
gallery:
  - "/assets/images/projects/circular-sensor-kit/prototype-01.jpg"
  - "/assets/images/projects/circular-sensor-kit/user-test-01.jpg"
contact:
  name: "Prof. Jelle Saldien"
  email: "jelle.saldien@uantwerpen.be"
summary: "A modular sensor platform exploring repairability, reconfiguration and circular electronics for citizen science."
---
```

### 13.2 Project body template

```md
## Challenge
Describe the societal, technological or design challenge.

## Design question
State the design or research question.

## Approach
Explain the design process, research method, prototyping approach or collaboration format.

## Prototype / demonstrator
Describe the tangible output.

## Results
Summarise the main findings or outcomes.

## Impact
Explain the relevance for users, society, sustainability, industry or education.

## Partners
List involved partners and their role.
```

---

## 14. Tone of voice voor websitecopy

### 14.1 Algemene toon

De tone of voice is:

- helder;
- actief;
- academisch onderbouwd;
- toegankelijk;
- niet te commercieel;
- niet te abstract;
- gericht op concrete ontwerpoutput.

### 14.2 Schrijfregels

Gebruik actieve zinnen.

Goed:

```text
We develop prototypes that help evaluate repairability, usability and circular value creation.
```

Minder goed:

```text
Prototypes are developed in order to facilitate the evaluation of repairability.
```

Koppel ontwerp altijd aan context.

Goed:

```text
The project explores how modular electronics can support longer product lifetimes in citizen science applications.
```

Minder goed:

```text
The project explores innovative modular technology.
```

### 14.3 Voorbeeldcopy homepage

```text
Product Development at the University of Antwerp connects design education and design research to address complex product challenges. We work with students, researchers and partners on prototypes, demonstrators and product-service systems that combine human needs, technological possibilities and circular strategies.
```

### 14.4 Voorbeeldcopy onderzoeksgroep

```text
The Product Development Research Group investigates how design can contribute to human-centered, sustainable and technology-driven product innovation. We combine human, technological and economic insights through design methods, prototypes and demonstrators.
```

### 14.5 Voorbeeldcopy opleiding

```text
The Product Development programme trains students to design meaningful products and product-service systems that go beyond form and function. Students learn to connect creativity, scientific reasoning, technology and societal relevance through studio-based design education.
```

---

## 15. Interactie en animatie

Gebruik subtiele interacties. De website moet professioneel en snel blijven.

Toegestaan:

- hover states op cards;
- subtiele transform van 1–2 px;
- fade-in bij scroll, indien toegankelijk en performant;
- zachte transitions op buttons en links;
- filterbare projectgrid.

Vermijd:

- zware parallax;
- trage intro-animaties;
- video als noodzakelijke content;
- flashy microinteractions zonder functie;
- animaties die de leesbaarheid hinderen.

Voorbeeld:

```css
.project-card {
  transition: transform 160ms ease, box-shadow 160ms ease;
}

.project-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-card);
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 16. Accessibility

De website moet minimaal voldoen aan goede basisprincipes voor toegankelijkheid.

Codex moet:

- semantische HTML gebruiken;
- duidelijke heading-hiërarchie toepassen;
- alt-teksten voorzien voor betekenisvolle beelden;
- decoratieve beelden leeg alt-attribuut geven;
- kleurcontrast controleren;
- toetsenbordnavigatie ondersteunen;
- focus states zichtbaar maken;
- links beschrijvend maken;
- geen informatie uitsluitend via kleur communiceren;
- responsive ontwerpen.

Voorbeeld focus state:

```css
:focus-visible {
  outline: 3px solid var(--ua-red);
  outline-offset: 3px;
}
```

---

## 17. Footer

De footer moet duidelijk de institutionele inbedding tonen.

Aanbevolen footer:

```text
Product Development / Productontwikkeling
Faculty of Design Sciences
University of Antwerp

Links:
- University of Antwerp
- Faculty of Design Sciences
- Product Development Research Group
- Contact
```

Voorbeeld HTML:

```html
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <img src="/assets/logos/ua-logo-negative.svg" alt="University of Antwerp" class="footer-logo" />
      <p>
        Product Development<br />
        Faculty of Design Sciences<br />
        University of Antwerp
      </p>
    </div>
    <nav aria-label="Footer navigation">
      <a href="/projects">Projects</a>
      <a href="/research">Research</a>
      <a href="/education">Education</a>
      <a href="/contact">Contact</a>
    </nav>
  </div>
</footer>
```

Voorbeeld CSS:

```css
.site-footer {
  background: var(--ua-blue);
  color: var(--color-white);
  padding: 3rem 0;
}

.site-footer a {
  color: var(--color-white);
  text-decoration-color: var(--fds-bluegrey);
}

.footer-logo {
  height: 44px;
  width: auto;
  margin-bottom: 1rem;
}
```

---

## 18. Referentie naar PowerPoint- en Word-template

Codex moet de templates niet automatisch uitlezen, maar ze gebruiken als visuele referentie wanneer ze door de gebruiker beschikbaar worden gemaakt.

### PowerPoint-template

Gebruik de PowerPoint-template als referentie voor:

- verhouding tussen beeld en tekst;
- gebruik van faculteitskleur;
- titelhiërarchie;
- afgeronde beeldkaders;
- witruimte;
- institutionele plaatsing van UA-logo.

Verwachte bestanden:

```text
templates/ua-powerpoint-template.pptx
templates/faculty-design-sciences-powerpoint-template.pptx
```

### Word-template

Gebruik de Word-template als referentie voor:

- formele teksthiërarchie;
- koppenstructuur;
- academische documenttoon;
- tabelstijl;
- kleuraccenten;
- documentmetadata.

Verwachte bestanden:

```text
templates/ua-word-template.docx
templates/faculty-design-sciences-word-template.docx
```

### Logo’s

Gebruik officiële logo’s uitsluitend als aangeleverde assets.

Verwachte bestanden:

```text
assets/logos/ua-logo-primary.svg
assets/logos/ua-logo-negative.svg
assets/logos/faculty-design-sciences-logo.svg
assets/logos/research-group-product-development-logo.svg
```

---

## 19. Do’s and don’ts voor Codex

### Do

- Gebruik de UA-huisstijl als basis.
- Gebruik `#82A1AD` als faculteitsaccent.
- Gebruik `#C8D9D8` voor zachte achtergrondvlakken.
- Gebruik `#002E65` voor structuur, titels en footer.
- Gebruik `#EA2C38` spaarzaam voor calls-to-action.
- Gebruik echte projectbeelden wanneer beschikbaar.
- Bouw projectcards modulair op.
- Maak de website responsive.
- Voorzie duidelijke alt-teksten.
- Maak content makkelijk uitbreidbaar via Markdown, JSON of MDX.

### Don’t

- Ontwerp geen nieuw logo voor Productontwikkeling.
- Gebruik geen fictieve of nagemaakte UA-logo’s.
- Gebruik geen overdadige gradients of flashy animaties.
- Gebruik geen generieke stockbeelden als primaire identiteit.
- Gebruik geen rood als dominante achtergrondkleur.
- Maak de site niet te commercieel of startup-achtig.
- Plaats niet te veel interne UA-logo’s naast elkaar.
- Verzin geen officiële claims, rankings of samenwerkingen.

---

## 20. Minimale implementatie-opdracht voor Codex

Gebruik onderstaande opdracht wanneer Codex de website moet genereren.

```text
Build a responsive portfolio website for Product Development / Productontwikkeling at the University of Antwerp, embedded in the Faculty of Design Sciences. Use the UA brand as the institutional basis and the Faculty of Design Sciences color palette as the visual accent.

Follow the styleguide in productontwikkeling_portfolio_styleguide.md.

Use the following local assets when available:
- assets/logos/ua-logo-primary.svg
- assets/logos/ua-logo-negative.svg
- assets/logos/faculty-design-sciences-logo.svg
- assets/logos/research-group-product-development-logo.svg
- templates/ua-powerpoint-template.pptx
- templates/faculty-design-sciences-powerpoint-template.pptx
- templates/ua-word-template.docx
- templates/faculty-design-sciences-word-template.docx

Do not create or simulate unofficial logos. If an asset is missing, use a textual placeholder and add a TODO comment.

Create:
- a homepage with hero, positioning, featured projects, research themes, education/student work, partners and contact section;
- a projects overview with filterable project cards;
- a project detail template using Markdown or JSON frontmatter;
- global CSS variables for the UA and Faculty of Design Sciences colors;
- reusable components for header, footer, project cards, theme cards, buttons and image cards;
- responsive and accessible HTML/CSS.

Visual direction:
- clean, academic, design-driven and spacious;
- strong use of white space;
- UA Blue for structure and headings;
- Faculty of Design Sciences blue-grey for accents;
- red only for important calls-to-action;
- rounded image cards and subtle shadows;
- real prototype, student, research and demonstrator imagery.
```

---

## 21. Checklist voor finale websitecontrole

Controleer voor publicatie:

- [ ] Officiële UA-logo’s zijn gebruikt en niet vervormd.
- [ ] De website maakt duidelijk dat Productontwikkeling onder UAntwerpen en de Faculteit Ontwerpwetenschappen valt.
- [ ] Er is geen apart, zelfontworpen opleidingslogo gebruikt.
- [ ] De faculteitskleur `#82A1AD` is correct toegepast.
- [ ] De pastelvariant `#C8D9D8` wordt alleen gebruikt als zachte achtergrond of labelkleur.
- [ ] UA-rood `#EA2C38` wordt spaarzaam gebruikt.
- [ ] Projectbeelden zijn inhoudelijk relevant.
- [ ] Alle projectcards hebben titel, type, jaar, samenvatting en tags.
- [ ] De website is bruikbaar op mobiel.
- [ ] Alt-teksten zijn voorzien.
- [ ] Focus states zijn zichtbaar.
- [ ] Links zijn beschrijvend.
- [ ] Contactinformatie is correct.
- [ ] Partners zijn correct vermeld.
- [ ] De algemene toon is helder, professioneel en ontwerpgericht.

---

## 22. Korte samenvatting voor developers

```text
Use UA as the master brand.
Use Faculty of Design Sciences blue-grey as the visual identity layer.
Use Product Development / Productontwikkeling as a textual identity, not as a separate logo.
Design clean, spacious, academic and prototype-driven pages.
Make project cards the core content component.
Use real images, clear metadata, tags and accessible markup.
Use official local logo and template assets when provided; never recreate them.
```
