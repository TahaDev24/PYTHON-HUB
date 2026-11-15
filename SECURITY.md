# Security Policy

Security is a core design requirement because PYTHON HUB may eventually discover, install, and execute third-party tools.

## Supported versions

Only the latest development branch is currently maintained. There are no stable releases yet.

## Reporting a vulnerability

Do not publish exploit details, credentials, proof-of-concept payloads, or sensitive logs in a public issue.

Use GitHub's private vulnerability reporting feature for this repository when it is enabled. If private reporting is unavailable, contact the repository maintainer through a private GitHub channel and include only the minimum information needed to establish the report.

A report should include the affected component, security impact and prerequisites, a minimal safe reproduction, and a suggested mitigation when known.

## Current security boundary

The present plugin registry is an in-process Python abstraction. It does not isolate code, restrict filesystem access, limit network access, or protect the host from malicious plugins. Do not load untrusted plugins.

Any future execution service must be designed around least privilege, explicit permissions, resource limits, auditability, and isolation before untrusted code is supported.
