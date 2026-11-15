# Documentation

Welcome to the PYTHON HUB engineering documentation.

## Start here

| Document | Purpose |
|---|---|
| [Getting Started](GETTING_STARTED.md) | Install the Python package and run the first commands |
| [Architecture](ARCHITECTURE.md) | Understand repository boundaries and runtime design |
| [Development](DEVELOPMENT.md) | Local workflow, quality checks, and testing |
| [Plugin System](PLUGIN_SYSTEM.md) | Tool contracts, registration, and integration rules |
| [Localization](LOCALIZATION.md) | English, Persian, RTL, and translation conventions |
| [Security Model](SECURITY_MODEL.md) | Trust boundaries and requirements for tool execution |
| [Roadmap](ROADMAP.md) | Planned phases and completion criteria |
| [Architecture Decisions](decisions/) | Records of important technical decisions |

## Documentation principles

- Document current behavior separately from proposed behavior.
- Include prerequisites and exact commands in setup instructions.
- Prefer small, focused pages over one enormous guide.
- Keep examples aligned with tested public interfaces.
- Update documentation when code, configuration, or user experience changes.

## Project terminology

- **Core:** shared runtime and platform contracts.
- **Category:** a navigational domain in the ecosystem catalog.
- **Tool:** a user-facing capability with a stable identifier and metadata.
- **Adapter:** an implementation that connects a tool to an upstream project or native capability.
- **Plugin:** a packaged extension that contributes one or more tools.
- **Integration:** a reviewed connection to an independently maintained project.
