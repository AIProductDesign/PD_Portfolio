import { content } from "./content.js";

const app = document.querySelector("#app");
const languageButtons = document.querySelectorAll(".language-button");
const brandLogo = document.querySelector("#brandLogo");
const defaultLanguage = "en";
let language = localStorage.getItem("portfolio-language") || defaultLanguage;
let activeFilters = new Set();
let activeAssignment = "all";
let searchQuery = "";

const dictionary = {
  en: {
    brandTitle: "Product Development / Productontwikkeling",
    brandSubtitle: "Faculty of Design Sciences — University of Antwerp",
    navProjects: "Projects",
    navAssignments: "Assignments",
    navArchive: "Archive",
    navAbout: "About",
    heroKicker: "Bachelor Proef 2025-2026",
    heroTitle: "Future product concepts by Product Development students",
    heroText: "A professional showcase of individual Bachelor Proef projects, created to inspire external partners, peer staff, and prospective students.",
    heroCtaProjects: "Explore projects",
    heroCtaAssignments: "View assignments",
    statYear: "Current year",
    statAssignments: "Assignments",
    statProjects: "Seed projects",
    sectionAssignments: "Assignment Themes",
    sectionFeatured: "Featured Projects",
    allProjects: "All Projects",
    searchPlaceholder: "Search by title, student, context, or keyword",
    filterAll: "All themes",
    empty: "No projects match the current filters.",
    poster: "Poster",
    presentation: "Presentation",
    visuals: "Visuals",
    projectContext: "Context",
    projectTarget: "Target group",
    projectAssets: "Project Assets",
    posterPreview: "Poster preview",
    briefContext: "Assignment Context",
    partners: "Partners",
    designChallenge: "Design challenge",
    designGoals: "Design goals",
    analysisFocus: "Analysis focus",
    courseObjectives: "Course objectives",
    sourceDocuments: "Source documents",
    backToProjects: "Back to projects",
    archiveTitle: "Archive",
    archiveText: "The portfolio is ready to grow across years and courses. The 2024-2025 archive is prepared as a placeholder until material is added.",
    aboutTitle: "About the Portfolio",
    aboutText: "This portfolio presents work from Product Development courses at the University of Antwerp. The first release focuses on Bachelor Proef 2025-2026 and is structured so future courses and academic years can be added.",
    footerCopyright: "Copyright University of Antwerp. Student work is shown for portfolio and collaboration purposes.",
    pendingAsset: "Pending",
  },
  nl: {
    brandTitle: "Productontwikkeling / Product Development",
    brandSubtitle: "Faculteit Ontwerpwetenschappen — Universiteit Antwerpen",
    navProjects: "Projecten",
    navAssignments: "Opdrachten",
    navArchive: "Archief",
    navAbout: "Over",
    heroKicker: "Bachelorproef 2025-2026",
    heroTitle: "Toekomstgerichte productconcepten van studenten Productontwikkeling",
    heroText: "Een professionele showcase van individuele bachelorproefprojecten, gemaakt om externe partners, collega-docenten en toekomstige studenten te inspireren.",
    heroCtaProjects: "Bekijk projecten",
    heroCtaAssignments: "Bekijk opdrachten",
    statYear: "Huidig jaar",
    statAssignments: "Opdrachten",
    statProjects: "Startprojecten",
    sectionAssignments: "Opdrachtthema's",
    sectionFeatured: "Uitgelichte Projecten",
    allProjects: "Alle Projecten",
    searchPlaceholder: "Zoek op titel, student, context of trefwoord",
    filterAll: "Alle thema's",
    empty: "Geen projecten gevonden voor deze filters.",
    poster: "Poster",
    presentation: "Presentatie",
    visuals: "Visuals",
    projectContext: "Context",
    projectTarget: "Doelgroep",
    projectAssets: "Projectmateriaal",
    posterPreview: "Posterweergave",
    briefContext: "Context Van De Opdracht",
    partners: "Partners",
    designChallenge: "Ontwerpuitdaging",
    designGoals: "Ontwerpdoelen",
    analysisFocus: "Analysefocus",
    courseObjectives: "Doelstellingen van het vak",
    sourceDocuments: "Brondocumenten",
    backToProjects: "Terug naar projecten",
    archiveTitle: "Archief",
    archiveText: "Het portfolio is voorbereid om te groeien over jaren en opleidingsonderdelen heen. Het archief 2024-2025 staat klaar als placeholder tot het materiaal wordt toegevoegd.",
    aboutTitle: "Over Het Portfolio",
    aboutText: "Dit portfolio toont werk uit opleidingsonderdelen Productontwikkeling aan de Universiteit Antwerpen. De eerste versie focust op Bachelorproef 2025-2026 en is zo opgebouwd dat toekomstige vakken en academiejaren kunnen worden toegevoegd.",
    footerCopyright: "Copyright Universiteit Antwerpen. Studentenwerk wordt getoond voor portfolio- en samenwerkingsdoeleinden.",
    pendingAsset: "Nog toe te voegen",
  },
};

function t(key) {
  return dictionary[language][key] || dictionary.en[key] || key;
}

function localize(value) {
  if (!value || typeof value === "string") return value || "";
  return value[language] || value.en || "";
}

function excerpt(text, maxWords = 34) {
  const words = text.split(/\s+/).filter(Boolean);
  if (words.length <= maxWords) return text;
  return `${words.slice(0, maxWords).join(" ")}...`;
}

function setLanguage(nextLanguage) {
  language = nextLanguage;
  localStorage.setItem("portfolio-language", language);
  document.documentElement.lang = language;
  if (brandLogo) {
    brandLogo.src = "Content/StyleGuide/UAntwerp%20logopakket/UA-hor-1-nl-rgb.svg";
    brandLogo.alt = language === "nl" ? "Universiteit Antwerpen" : "University of Antwerp";
  }
  languageButtons.forEach((button) => {
    button.classList.toggle("is-active", button.dataset.language === language);
  });
  document.querySelectorAll("[data-i18n]").forEach((node) => {
    node.textContent = t(node.dataset.i18n);
  });
  render();
}

function normalize(text) {
  return text.toLowerCase().normalize("NFD").replace(/\p{Diacritic}/gu, "");
}

function getAssignment(id) {
  return content.assignments.find((assignment) => assignment.id === id);
}

function getProjects() {
  return content.projects.filter((project) => {
    const matchesAssignment = activeAssignment === "all" || project.assignmentId === activeAssignment;
    const matchesTags = activeFilters.size === 0 || [...activeFilters].every((tag) => project.tags.includes(tag));
    const haystack = normalize([
      localize(project.title),
      project.student,
      localize(project.summary),
      localize(project.context),
      localize(project.targetGroup),
      project.tags.join(" "),
    ].join(" "));
    return matchesAssignment && matchesTags && haystack.includes(normalize(searchQuery));
  });
}

function allTags() {
  return [...new Set(content.projects.flatMap((project) => project.tags))].sort();
}

function assetLink(asset, label) {
  if (!asset) return `<span class="asset-missing">${t("pendingAsset")} ${label}</span>`;
  return `<a class="asset-link" href="${asset}" target="_blank" rel="noreferrer">${label}</a>`;
}

function visualGallery(visuals) {
  if (!visuals || visuals.length === 0) {
    return `<span class="asset-missing">${t("pendingAsset")} ${t("visuals")}</span>`;
  }
  return `
    <div class="visual-gallery">
      ${visuals.map((visual, index) => `
        <a href="${visual}" target="_blank" rel="noreferrer">
          <img src="${visual}" alt="${t("visuals")} ${index + 1}" loading="lazy" onerror="this.closest('a').remove();">
        </a>
      `).join("")}
    </div>
  `;
}

function posterEmbed(poster, posterPreview) {
  if (!poster && !posterPreview) return `<span class="asset-missing">${t("pendingAsset")} ${t("poster")}</span>`;
  if (!poster && posterPreview) {
    return `
      <figure class="poster-viewer">
        <figcaption>${t("posterPreview")}</figcaption>
        <a href="${posterPreview}" target="_blank" rel="noreferrer">
          <img src="${posterPreview}" alt="${t("posterPreview")}" loading="lazy">
        </a>
      </figure>
    `;
  }
  return `
    <figure class="poster-viewer">
      <figcaption>${t("posterPreview")}</figcaption>
      <iframe src="${poster}#toolbar=0&navpanes=0" title="${t("posterPreview")}" loading="lazy"></iframe>
    </figure>
  `;
}

function localizedList(items) {
  const list = localize(items);
  if (!Array.isArray(list) || list.length === 0) return "";
  return `<ul>${list.map((item) => `<li>${item}</li>`).join("")}</ul>`;
}

function sourceDocumentLinks(documents = []) {
  if (!documents.length) return "";
  return `
    <div class="source-links">
      ${documents.map((document) => `
        <a href="${document.path}" target="_blank" rel="noreferrer">${localize(document.label)}</a>
      `).join("")}
    </div>
  `;
}

function courseContext() {
  const course = content.courses[0];
  const sourceLinks = sourceDocumentLinks(course.sourceDocuments);
  return `
    <section class="context-band">
      <div>
        <p class="kicker">Bachelor Proef</p>
        <h2>${t("courseObjectives")}</h2>
        ${localizedList(course.objectives)}
      </div>
      ${sourceLinks ? `<div>
        <p class="kicker">2025-2026</p>
        <h2>${t("sourceDocuments")}</h2>
        ${sourceLinks}
      </div>` : ""}
    </section>
  `;
}

function assignmentBrief(assignment) {
  if (!assignment.brief) return "";
  return `
    <section class="brief-section">
      <div class="section-heading">
        <p class="kicker">${t("briefContext")}</p>
        <h2>${t("designChallenge")}</h2>
      </div>
      <div class="brief-grid">
        <article class="brief-card is-wide">
          <span>${t("partners")}</span>
          <strong>${assignment.brief.partners}</strong>
          <p>${localize(assignment.brief.challenge)}</p>
          <p>${localize(assignment.brief.background)}</p>
        </article>
        <article class="brief-card">
          <span>${t("designGoals")}</span>
          ${localizedList(assignment.brief.goals)}
        </article>
        <article class="brief-card">
          <span>${t("analysisFocus")}</span>
          ${localizedList(assignment.brief.analysisFocus)}
        </article>
      </div>
    </section>
  `;
}

function assignmentCard(assignment) {
  return `
    <article class="assignment-card" style="--accent:${assignment.color}">
      <div>
        <p class="kicker">${assignment.course} · ${assignment.year}</p>
        <h3>${localize(assignment.title)}</h3>
        <p>${localize(assignment.description)}</p>
      </div>
      <a href="#/assignment/${assignment.id}">${localize({ en: "View theme", nl: "Bekijk thema" })}</a>
    </article>
  `;
}

function projectCard(project) {
  const assignment = getAssignment(project.assignmentId);
  const thumbnail = project.assets.thumbnail || "assets/placeholders/project-placeholder.svg";
  return `
    <article class="project-card">
      <a href="#/project/${project.id}" aria-label="${localize(project.title)}">
        <img src="${thumbnail}" alt="" loading="lazy" onerror="this.onerror=null;this.src='assets/placeholders/project-placeholder.svg';">
        <div class="project-card-body">
          <p class="theme-label" style="--accent:${assignment.color}">${localize(assignment.title)}</p>
          <h3>${localize(project.title)}</h3>
          <p class="student">${project.student}</p>
          <p>${excerpt(localize(project.summary))}</p>
          <div class="tag-list">${project.tags.slice(0, 4).map((tag) => `<span>${tag}</span>`).join("")}</div>
        </div>
      </a>
    </article>
  `;
}

function renderHome() {
  const featured = content.projects.filter((project) => project.featured).slice(0, 3);
  return `
    <section class="hero">
      <div class="hero-copy">
        <p class="kicker">${t("heroKicker")}</p>
        <h1>${t("heroTitle")}</h1>
        <p>${t("heroText")}</p>
        <div class="hero-actions">
          <a class="button primary" href="#/projects">${t("heroCtaProjects")}</a>
          <a class="button secondary" href="#/assignments">${t("heroCtaAssignments")}</a>
        </div>
      </div>
      <div class="hero-panel" aria-label="Portfolio statistics">
        <div><strong>2025-2026</strong><span>${t("statYear")}</span></div>
        <div><strong>${content.assignments.length}</strong><span>${t("statAssignments")}</span></div>
        <div><strong>${content.projects.length}</strong><span>${t("statProjects")}</span></div>
      </div>
    </section>
    <section class="section">
      <div class="section-heading">
        <p class="kicker">${content.courses[0].year}</p>
        <h2>${t("sectionAssignments")}</h2>
      </div>
      <div class="assignment-grid">${content.assignments.map(assignmentCard).join("")}</div>
    </section>
    <section class="section">
      <div class="section-heading">
        <p class="kicker">${content.courses[0].name}</p>
        <h2>${t("sectionFeatured")}</h2>
      </div>
      <div class="project-grid">${featured.map(projectCard).join("")}</div>
    </section>
  `;
}

function renderProjects() {
  const projects = getProjects();
  return `
    <section class="page-intro">
      <p class="kicker">Bachelor Proef · 2025-2026</p>
      <h1>${t("allProjects")}</h1>
      <p>${localize(content.courses[0].description)}</p>
    </section>
    <section class="toolbar" aria-label="Project filters">
      <input class="search-input" type="search" value="${searchQuery}" placeholder="${t("searchPlaceholder")}" aria-label="${t("searchPlaceholder")}">
      <div class="segmented">
        <button type="button" class="${activeAssignment === "all" ? "is-active" : ""}" data-assignment="all">${t("filterAll")}</button>
        ${content.assignments.map((assignment) => `<button type="button" class="${activeAssignment === assignment.id ? "is-active" : ""}" data-assignment="${assignment.id}">${localize(assignment.title)}</button>`).join("")}
      </div>
      <div class="filter-chips">
        ${allTags().map((tag) => `<button type="button" class="${activeFilters.has(tag) ? "is-active" : ""}" data-tag="${tag}">${tag}</button>`).join("")}
      </div>
    </section>
    <section class="project-grid" aria-live="polite">
      ${projects.length ? projects.map(projectCard).join("") : `<p class="empty-state">${t("empty")}</p>`}
    </section>
  `;
}

function renderAssignments() {
  return `
    <section class="page-intro">
      <p class="kicker">Bachelor Proef · 2025-2026</p>
      <h1>${t("sectionAssignments")}</h1>
      <p>${localize(content.courses[0].description)}</p>
    </section>
    ${courseContext()}
    <section class="assignment-grid">${content.assignments.map(assignmentCard).join("")}</section>
  `;
}

function renderAssignment(id) {
  const assignment = getAssignment(id);
  if (!assignment) return renderNotFound();
  const projects = content.projects.filter((project) => project.assignmentId === id);
  return `
    <section class="page-intro assignment-intro" style="--accent:${assignment.color}">
      <p class="kicker">${assignment.course} · ${assignment.year}</p>
      <h1>${localize(assignment.title)}</h1>
      <p>${localize(assignment.longDescription)}</p>
    </section>
    ${assignmentBrief(assignment)}
    <section class="project-grid">${projects.map(projectCard).join("")}</section>
  `;
}

function renderProject(id) {
  const project = content.projects.find((item) => item.id === id);
  if (!project) return renderNotFound();
  const assignment = getAssignment(project.assignmentId);
  const hero = project.assets.thumbnail || "assets/placeholders/project-placeholder.svg";
  return `
    <article class="project-detail">
      <a class="back-link" href="#/projects">${t("backToProjects")}</a>
      <header class="project-hero" style="--accent:${assignment.color}">
        <div>
          <p class="theme-label">${localize(assignment.title)} · ${assignment.year}</p>
          <h1>${localize(project.title)}</h1>
          <p class="student">${project.student}</p>
          <p>${localize(project.summary)}</p>
          <div class="tag-list">${project.tags.map((tag) => `<span>${tag}</span>`).join("")}</div>
        </div>
        <img src="${hero}" alt="" onerror="this.onerror=null;this.src='assets/placeholders/project-placeholder.svg';">
      </header>
      <section class="detail-grid">
        <div>
          <h2>${t("projectContext")}</h2>
          <p>${localize(project.context)}</p>
        </div>
        <div>
          <h2>${t("projectTarget")}</h2>
          <p>${localize(project.targetGroup)}</p>
        </div>
      </section>
      <section class="asset-section">
        <h2>${t("projectAssets")}</h2>
        ${posterEmbed(project.assets.poster, project.assets.posterPreview)}
        <div class="asset-grid">
          ${assetLink(project.assets.presentation, t("presentation"))}
        </div>
        ${visualGallery(project.assets.visuals)}
      </section>
    </article>
  `;
}

function renderArchive() {
  return `
    <section class="page-intro">
      <p class="kicker">Portfolio Product Development</p>
      <h1>${t("archiveTitle")}</h1>
      <p>${t("archiveText")}</p>
    </section>
    <section class="year-list">
      ${content.years.map((year) => `
        <article>
          <strong>${year.label}</strong>
          <span>${localize(year.status)}</span>
        </article>
      `).join("")}
    </section>
  `;
}

function renderAbout() {
  return `
    <section class="page-intro">
      <p class="kicker">University of Antwerp</p>
      <h1>${t("aboutTitle")}</h1>
      <p>${t("aboutText")}</p>
    </section>
    <section class="about-panel">
      <h2>Copyright</h2>
      <p>${t("footerCopyright")}</p>
    </section>
  `;
}

function renderNotFound() {
  return `
    <section class="page-intro">
      <h1>Page not found</h1>
      <p><a href="#/">Return home</a></p>
    </section>
  `;
}

function route() {
  const [, section = "", id = ""] = window.location.hash.split("/");
  if (section === "projects") return renderProjects();
  if (section === "assignments") return renderAssignments();
  if (section === "assignment") return renderAssignment(id);
  if (section === "project") return renderProject(id);
  if (section === "archive") return renderArchive();
  if (section === "about") return renderAbout();
  return renderHome();
}

function bindInteractions() {
  const searchInput = app.querySelector(".search-input");
  if (searchInput) {
    searchInput.addEventListener("input", (event) => {
      searchQuery = event.target.value;
      render();
      app.querySelector(".search-input")?.focus();
    });
  }

  app.querySelectorAll("[data-assignment]").forEach((button) => {
    button.addEventListener("click", () => {
      activeAssignment = button.dataset.assignment;
      render();
    });
  });

  app.querySelectorAll("[data-tag]").forEach((button) => {
    button.addEventListener("click", () => {
      const tag = button.dataset.tag;
      if (activeFilters.has(tag)) activeFilters.delete(tag);
      else activeFilters.add(tag);
      render();
    });
  });
}

function render() {
  app.innerHTML = route();
  bindInteractions();
}

languageButtons.forEach((button) => {
  button.addEventListener("click", () => setLanguage(button.dataset.language));
});

window.addEventListener("hashchange", render);
setLanguage(language);
