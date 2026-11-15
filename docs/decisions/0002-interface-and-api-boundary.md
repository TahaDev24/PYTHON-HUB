# ADR 0002: Separate the Web Client from the Python Core

- Status: Accepted
- Date: 2026-11-15

## Context

The product must offer a high-quality responsive interface on phones and computers while keeping the core Python tools reusable from a command line and other clients.

## Decision

Keep the web interface in apps/web and the Python runtime in src/python_hub. Use a versioned HTTP API for future client-server interaction. The initial web shell is static and does not pretend to be connected to unfinished services.

## Consequences

- The same Python capabilities can later serve web and desktop clients.
- Frontend technology can evolve independently from the Python package.
- API schemas must be versioned and tested.
- The project must document which interface actions are local-only and which are backed by server capabilities.
