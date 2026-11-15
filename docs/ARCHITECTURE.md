# Architecture

## Architectural direction

PYTHON HUB is intended to become a multi-surface developer platform. The repository begins as a modular monolith: one Python distribution with explicit internal boundaries and an independently served web interface.

## System context

~~~text
             +--------------------------+
             |      PYTHON HUB USERS    |
             +------------+-------------+
                          |
             +------------+-------------+
             |                          |
      +------v-------+           +------v------+
      | Responsive   |           | Python CLI  |
      | Web Client   |           | Local tools |
      +------+-------+           +------+------+
             |                          |
             +------------+-------------+
                          |
                  +-------v-------+
                  | Optional API  |
                  +-------+-------+
                          |
                  +-------v-------+
                  |   Core Layer  |
                  +-------+-------+
                          |
        +-----------------+------------------+
        |                 |                  |
   +----v----+      +-----v-----+     +------v------+
   | Catalog |      | Plugins   |     | Localization|
   +---------+      +-----+-----+     +-------------+
                           |
                    +------v-------+
                    | Tool Adapters|
                    | Future work  |
                    +--------------+
~~~

## Repository boundaries

The installable Python package lives under src/python_hub:

- cli: command-line parsing and user-facing commands.
- core: configuration, paths, logging, and domain errors.
- catalog: stable category models and taxonomy.
- plugins: public contracts and the initial in-process registry.
- localization: message catalogs and locale metadata.
- api: optional HTTP application.

The current web application lives under apps/web and uses browser-native technologies. It is a responsive interface foundation, not yet an API-connected production client.

## Dependency direction

- API and CLI may call application or domain services.
- Catalog and plugin contracts should not depend on web presentation code.
- Tool adapters depend on stable contracts, not on CLI or API handlers.
- Localization keys are presentation resources and should not become domain identifiers.

Avoid circular imports and keep optional API dependencies out of the minimal core installation.

## Execution lifecycle (planned)

1. Discover a tool definition from a trusted catalog or installed plugin.
2. Resolve the selected adapter and declared requirements.
3. Validate inputs against a schema.
4. Check permissions and execution policy.
5. Execute inside an approved isolation boundary.
6. Normalize output, errors, and logs.
7. Record an auditable result for the user.

Only metadata and registry foundations exist today. The secure execution lifecycle is future work.

## Quality attributes

Prioritize portability, responsiveness, accessibility, deterministic behavior, minimal core dependencies, explicit permissions, provenance, and graceful handling of unavailable integrations. Clearly separate installed, available, and planned tools.
