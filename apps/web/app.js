const domains = [
  ["code-development","Code Development","Editors, language servers, navigation, and coding workflows.","⌘"],
  ["code-quality","Code Quality","Linting, formatting, type checking, and refactoring.","◇"],
  ["security-auditing","Security & Auditing","Dependency review, static analysis, and security reporting.","⬡"],
  ["testing-debugging","Testing & Debugging","Test runners, debugging, coverage, and profiling.","⌁"],
  ["artificial-intelligence","Artificial Intelligence","Machine learning, deep learning, NLP, and model tooling.","✳"],
  ["data-engineering","Data Engineering","Dataframes, numerical computing, ETL, and pipelines.","▥"],
  ["database-systems","Database Systems","SQL clients, ORM, migrations, and database utilities.","▤"],
  ["web-api","Web & API Development","Web frameworks, API clients, and service development.","⌘"],
  ["networking","Networking","HTTP, sockets, DNS, protocols, and diagnostics.","⌁"],
  ["automation","Automation","Task automation, scheduling, and workflow orchestration.","⟳"],
  ["file-processing","File Processing","Documents, archives, images, audio, and video formats.","▧"],
  ["visualization","Visualization","Charts, dashboards, reports, and visual analytics.","◒"],
  ["package-management","Package Management","Packages, virtual environments, dependency locking.","⬡"],
  ["devops-deployment","DevOps & Deployment","Containers, CI/CD, deployment, and release tooling.","⏣"],
  ["system-utilities","System Utilities","Processes, filesystems, system metrics, and OS utilities.","⌬"],
  ["gui-development","GUI Development","Desktop interfaces, widgets, and application packaging.","▣"],
  ["scientific-computing","Scientific Computing","Numerical methods, simulation, and research workflows.","∑"],
  ["documentation","Documentation","Documentation generation, API references, and publishing.","▧"]
];
const copy = {
  en: {
    workspace:"WORKSPACE", overview:"Overview", ecosystem:"Ecosystem", favorites:"Favorites", discover:"DISCOVER",
    early:"Early foundation", earlyText:"The platform is taking shape.", settings:"Settings", creator:"Creator",
    heroEyebrow:"THE PYTHON ECOSYSTEM, CONNECTED", heroLineOne:"Your Python world.", heroLineTwo:"One workspace.",
    heroDescription:"Explore the tools, workflows, and technologies that power modern Python development — all through one evolving platform.",
    explore:"Explore ecosystem", heroCaption:"18 domains · One unified vision", directory:"THE DIRECTORY",
    domainsTitle:"Explore the ecosystem", domainsSubtitle:"A map of the Python domains this platform is designed to bring together.",
    clear:"Clear search", noResults:"No matching domains", trySearch:"Try another search term.",
    footerBy:"Built by TahaDev24", foundationStatus:"FOUNDATION PREVIEW", search:"Search ecosystem...",
    favoritesTitle:"Your favorites", favoritesSubtitle:"The domains you have saved for quick access.", settingsTitle:"Workspace settings",
    settingsSubtitle:"Personalize the interface language and explore the current platform foundation."
  },
  fa: {
    workspace:"محیط کار", overview:"نمای کلی", ecosystem:"اکوسیستم", favorites:"علاقه‌مندی‌ها", discover:"کشف ابزارها",
    early:"نسخه زیرساختی", earlyText:"پلتفرم در حال شکل‌گیری است.", settings:"تنظیمات", creator:"سازنده",
    heroEyebrow:"اکوسیستم پایتون، یکپارچه", heroLineOne:"دنیای پایتون تو.", heroLineTwo:"در یک محیط کاری.",
    heroDescription:"ابزارها، گردش‌کارها و فناوری‌های توسعه مدرن پایتون را در یک پلتفرم در حال تکامل کشف کن.",
    explore:"کاوش اکوسیستم", heroCaption:"۱۸ حوزه تخصصی · یک چشم‌انداز یکپارچه", directory:"فهرست حوزه‌ها",
    domainsTitle:"اکوسیستم را کشف کن", domainsSubtitle:"نقشه‌ای از حوزه‌های پایتون که این پلتفرم برای یکپارچه‌سازی آن‌ها طراحی شده است.",
    clear:"پاک‌کردن جست‌وجو", noResults:"حوزه‌ای پیدا نشد", trySearch:"عبارت دیگری را جست‌وجو کن.",
    footerBy:"ساخته‌شده توسط TahaDev24", foundationStatus:"پیش‌نمایش زیرساخت", search:"جست‌وجو در اکوسیستم...",
    favoritesTitle:"علاقه‌مندی‌های تو", favoritesSubtitle:"حوزه‌هایی که برای دسترسی سریع ذخیره کرده‌ای.", settingsTitle:"تنظیمات محیط کار",
    settingsSubtitle:"زبان رابط را شخصی‌سازی کن و وضعیت فعلی زیرساخت را ببین."
  }
};
const namesFa = {
  "code-development":"توسعه کد","code-quality":"کیفیت کد","security-auditing":"امنیت و ممیزی",
  "testing-debugging":"تست و اشکال‌زدایی","artificial-intelligence":"هوش مصنوعی","data-engineering":"مهندسی داده",
  "database-systems":"سیستم‌های پایگاه داده","web-api":"توسعه وب و API","networking":"شبکه",
  "automation":"اتوماسیون","file-processing":"پردازش فایل","visualization":"مصورسازی داده",
  "package-management":"مدیریت پکیج","devops-deployment":"DevOps و استقرار","system-utilities":"ابزارهای سیستمی",
  "gui-development":"توسعه رابط کاربری","scientific-computing":"محاسبات علمی","documentation":"مستندسازی"
};
const descriptionsFa = {
  "code-development":"ویرایشگرها، سرورهای زبان، پیمایش کد و گردش‌کار توسعه.",
  "code-quality":"بررسی سبک، قالب‌بندی، بررسی نوع و بازآرایی کد.",
  "security-auditing":"بررسی وابستگی‌ها، تحلیل ایستا و گزارش امنیتی.",
  "testing-debugging":"اجرای تست، اشکال‌زدایی، پوشش تست و پروفایلینگ.",
  "artificial-intelligence":"یادگیری ماشین، یادگیری عمیق، پردازش زبان و ابزار مدل‌ها.",
  "data-engineering":"دیتافریم، محاسبات عددی، ETL و پایپ‌لاین داده.",
  "database-systems":"ابزار SQL، ORM، مهاجرت و مدیریت پایگاه داده.",
  "web-api":"فریم‌ورک‌های وب، کلاینت API و توسعه سرویس.",
  "networking":"HTTP، سوکت، DNS، پروتکل‌ها و عیب‌یابی شبکه.",
  "automation":"خودکارسازی وظایف، زمان‌بندی و هماهنگ‌سازی گردش‌کار.",
  "file-processing":"پردازش سند، آرشیو، تصویر، صوت و ویدئو.",
  "visualization":"نمودار، داشبورد، گزارش و تحلیل بصری.",
  "package-management":"پکیج‌ها، محیط مجازی و مدیریت وابستگی‌ها.",
  "devops-deployment":"کانتینر، CI/CD، استقرار و انتشار.",
  "system-utilities":"پردازش‌ها، فایل‌سیستم و سنجه‌های سیستم‌عامل.",
  "gui-development":"رابط دسکتاپ، ویجت و بسته‌بندی اپلیکیشن.",
  "scientific-computing":"روش‌های عددی، شبیه‌سازی و گردش‌کار پژوهشی.",
  "documentation":"تولید مستندات، مرجع API و انتشار دانش."
};
let locale = localStorage.getItem("python-hub-locale") === "fa" ? "fa" : "en";
let currentView = "overview";
let searchTerm = "";
let favorites = new Set(JSON.parse(localStorage.getItem("python-hub-favorites") || "[]"));
const $ = (selector) => document.querySelector(selector);
const t = (key) => copy[locale][key] || copy.en[key] || key;

function renderViewLabels() {
  $("#breadcrumb-current").textContent = currentView === "favorites" ? t("favorites") : currentView === "settings" ? t("settings") : currentView === "ecosystem" ? t("ecosystem") : t("overview");
  $("#section-title").textContent = currentView === "favorites" ? t("favoritesTitle") : currentView === "settings" ? t("settingsTitle") : t("domainsTitle");
  $("#section-subtitle").textContent = currentView === "favorites" ? t("favoritesSubtitle") : currentView === "settings" ? t("settingsSubtitle") : t("domainsSubtitle");
}
function applyLocale() {
  document.documentElement.lang = locale;
  document.documentElement.dir = locale === "fa" ? "rtl" : "ltr";
  document.querySelectorAll("[data-i18n]").forEach((node) => {
    const key = node.getAttribute("data-i18n");
    if (copy[locale][key]) node.textContent = copy[locale][key];
  });
  $("#search-input").placeholder = t("search");
  $("#language-toggle").innerHTML = locale === "en" ? "FA <span>⌄</span>" : "EN <span>⌄</span>";
  renderViewLabels();
  renderDomains();
}
function renderDomains() {
  const grid = $("#category-grid");
  if (currentView === "settings") {
    grid.innerHTML = locale === "fa"
      ? '<article class="category-card"><div class="card-top"><span class="category-icon">文</span></div><strong>زبان رابط کاربری</strong><p>انگلیسی زبان پیش‌فرض است و فارسی با چیدمان راست‌به‌چپ پشتیبانی می‌شود.</p><button class="filter-button" id="settings-language">تغییر زبان</button></article><article class="category-card"><div class="card-top"><span class="category-icon">◈</span></div><strong>وضعیت پلتفرم</strong><p>مخزن در حال حاضر زیرساخت اولیه را دارد؛ اجرای ابزارها و یکپارچه‌سازی‌ها در برنامه توسعه هستند.</p></article>'
      : '<article class="category-card"><div class="card-top"><span class="category-icon">文</span></div><strong>Interface language</strong><p>English is the default language. Persian is available with right-to-left layout support.</p><button class="filter-button" id="settings-language">Switch language</button></article><article class="category-card"><div class="card-top"><span class="category-icon">◈</span></div><strong>Platform status</strong><p>The current repository contains the initial foundation. Tool execution and integrations are planned work.</p></article>';
    $("#result-count").textContent = locale === "fa" ? "تنظیمات" : "SETTINGS";
    $("#empty-state").hidden = true;
    const switchButton = $("#settings-language");
    if (switchButton) switchButton.addEventListener("click", toggleLocale);
    return;
  }
  const visible = domains.filter((item) => {
    const matchesSearch = (item[1] + " " + item[2] + " " + (namesFa[item[0]] || "")).toLowerCase().includes(searchTerm);
    const matchesView = currentView !== "favorites" || favorites.has(item[0]);
    return matchesSearch && matchesView;
  });
  grid.innerHTML = visible.map((item) => {
    const title = locale === "fa" ? namesFa[item[0]] : item[1];
    const description = locale === "fa" ? descriptionsFa[item[0]] : item[2];
    return '<button class="category-card" data-category="' + item[0] + '" aria-label="' + title + '">' +
      '<span class="card-top"><span class="category-icon">' + item[3] + '</span><span class="card-arrow">' + (favorites.has(item[0]) ? "★" : "↗") + '</span></span>' +
      '<strong>' + title + '</strong><p>' + description + '</p></button>';
  }).join("");
  $("#result-count").textContent = locale === "fa" ? visible.length + " حوزه" : visible.length + " DOMAINS";
  $("#empty-state").hidden = visible.length !== 0;
  $("#clear-search").hidden = searchTerm.length === 0;
  grid.querySelectorAll("[data-category]").forEach((card) => card.addEventListener("click", () => toggleFavorite(card.dataset.category)));
}
function toggleFavorite(id) {
  if (favorites.has(id)) favorites.delete(id);
  else favorites.add(id);
  localStorage.setItem("python-hub-favorites", JSON.stringify(Array.from(favorites)));
  renderDomains();
}
function toggleLocale() {
  locale = locale === "en" ? "fa" : "en";
  localStorage.setItem("python-hub-locale", locale);
  applyLocale();
}
function setView(view) {
  currentView = view;
  document.querySelectorAll(".nav-item[data-view]").forEach((button) => button.classList.toggle("active", button.dataset.view === view));
  renderViewLabels();
  $("#catalog-section").scrollIntoView({ behavior: "smooth", block: "start" });
  $("#sidebar").classList.remove("open");
  renderDomains();
}
$("#language-toggle").addEventListener("click", toggleLocale);
$("#search-input").addEventListener("input", (event) => { searchTerm = event.target.value.trim().toLowerCase(); renderDomains(); });
$("#clear-search").addEventListener("click", () => { searchTerm = ""; $("#search-input").value = ""; renderDomains(); });
$("#explore-button").addEventListener("click", () => setView("ecosystem"));
$("#menu-toggle").addEventListener("click", () => $("#sidebar").classList.toggle("open"));
document.querySelectorAll(".nav-item[data-view]").forEach((button) => button.addEventListener("click", () => setView(button.dataset.view)));
document.addEventListener("keydown", (event) => {
  if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") { event.preventDefault(); $("#search-input").focus(); }
  if (event.key === "Escape") $("#sidebar").classList.remove("open");
});
applyLocale();
