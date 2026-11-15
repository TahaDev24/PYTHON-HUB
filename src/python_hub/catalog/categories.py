"""Initial taxonomy for the Python ecosystem."""

from python_hub.catalog.models import Category

_CATEGORIES: tuple[Category, ...] = (
    Category("code-development", "Code Development", "Editors, language servers, navigation, and developer workflows."),
    Category("code-quality", "Code Quality", "Linting, formatting, type checking, refactoring, and maintainability."),
    Category("security-auditing", "Security & Auditing", "Dependency review, static analysis, secrets detection, and security reporting."),
    Category("testing-debugging", "Testing & Debugging", "Test runners, debugging, coverage, profiling, and diagnostics."),
    Category("artificial-intelligence", "Artificial Intelligence", "Machine learning, deep learning, NLP, and model tooling."),
    Category("data-engineering", "Data Engineering", "Dataframes, numerical computing, ETL, pipelines, and validation."),
    Category("database-systems", "Database Systems", "SQL clients, ORM, migrations, and database utilities."),
    Category("web-api", "Web & API Development", "Web frameworks, API clients, schema tools, and service development."),
    Category("networking", "Networking", "HTTP, sockets, DNS, protocol clients, and network diagnostics."),
    Category("automation", "Automation", "Task automation, scheduling, workflow orchestration, and scripting."),
    Category("file-processing", "File Processing", "Documents, archives, images, audio, video, and structured file formats."),
    Category("visualization", "Visualization", "Charts, dashboards, reports, and interactive visual analytics."),
    Category("package-management", "Package Management", "Package discovery, virtual environments, dependency locking, and publishing."),
    Category("devops-deployment", "DevOps & Deployment", "Containers, CI/CD, deployment, observability, and release tooling."),
    Category("system-utilities", "System Utilities", "Processes, filesystems, system metrics, and operating-system integration."),
    Category("gui-development", "GUI Development", "Desktop interfaces, widgets, cross-platform UI, and packaging."),
    Category("scientific-computing", "Scientific Computing", "Numerical methods, simulation, symbolic mathematics, and research workflows."),
    Category("documentation", "Documentation", "Documentation generation, API references, diagrams, and knowledge publishing."),
)


def get_categories() -> tuple[Category, ...]:
    """Return the stable, read-only list of ecosystem categories."""
    return _CATEGORIES


def get_category(category_id: str) -> Category | None:
    """Find a category by its stable identifier."""
    normalized = category_id.strip().lower()
    return next((item for item in _CATEGORIES if item.id == normalized), None)
