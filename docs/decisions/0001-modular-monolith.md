# ADR 0001: Start with a Modular Monolith

- Status: Accepted
- Date: 2026-11-15

## Context

PYTHON HUB has a broad product vision but is at the beginning of implementation. Splitting the first version into many network services would add deployment, observability, and operational complexity before the boundaries are understood.

## Decision

Start with one installable Python distribution organized into explicit modules. Keep the web interface as a separate client and expose a versioned API boundary where needed.

## Consequences

Positive:
- Simple local setup and contributor onboarding.
- Easy unit testing without network infrastructure.
- Shared types and domain rules remain close together.
- Modules can be extracted later when justified by scale or security.

Trade-offs:
- Module boundaries need discipline to avoid hidden coupling.
- The API and UI need explicit contracts as they evolve.
- The initial process is not an isolation boundary for untrusted plugins.
