"""Immutable models for catalog entries."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Category:
    """A high-level domain in the Python ecosystem."""

    id: str
    name: str
    description: str
