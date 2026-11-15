# Plugin System

## Purpose

The plugin system is the long-term extension boundary for bringing independently maintained Python tools into one consistent workspace.

The current implementation contains a typed contract and an in-process registry. It is an internal foundation only.

## Current contract

A tool exposes a stable identifier, display name, short description, catalog category identifier, version, permission labels, and an execute method that accepts a context and parameter mapping and returns a normalized result.

The contract is defined in src/python_hub/plugins/contracts.py.

## Current registry

ToolRegistry supports registration by stable identifier, duplicate identifier rejection, lookup, ordered listing, and atomic batch registration.

The registry does not discover packages, resolve dependencies, verify signatures, execute subprocesses, or isolate code.

## Proposed plugin package manifest

The following is a design proposal, not a supported manifest format yet.

~~~json
{
  "schema_version": 1,
  "id": "example.image-tools",
  "name": "Example Image Tools",
  "version": "1.0.0",
  "publisher": "Example Publisher",
  "description": "Image utilities for the workspace.",
  "category": "file-processing",
  "entry_point": "example_plugin:create_plugin",
  "permissions": ["filesystem.read.user-selected"],
  "supported_platforms": ["windows", "macos", "linux"]
}
~~~

## Integration review

Every integration must be reviewed for upstream identity and maintenance, license compatibility, supported Python and operating-system versions, installation source, dependency footprint, declared permissions, update strategy, known vulnerabilities, and test coverage.

Prefer official APIs and stable Python interfaces. Do not scrape websites or depend on undocumented behavior when a supported interface exists.

## Future lifecycle

A future plugin lifecycle may include discovery, verification, installation, permission review, activation, update, disablement, and removal. These operations must be explicit and reversible.

## Security requirement

A Python plugin can execute arbitrary code with the privileges of its process. Metadata declarations are not a sandbox. Untrusted plugin execution must not be introduced until isolation, permissions, resource limits, logging, and recovery are implemented and tested.
