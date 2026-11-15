"""Public contracts for tools and plugins.

The contract defines metadata and invocation shape only. It does not provide
process isolation or make an implementation safe to execute.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Protocol


@dataclass(frozen=True, slots=True)
class ToolContext:
    """Execution context passed to a tool implementation."""

    data_dir: str
    locale: str = "en"


@dataclass(frozen=True, slots=True)
class ToolResult:
    """Normalized result returned by a tool."""

    success: bool
    message: str
    data: Mapping[str, object] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ToolMetadata:
    """Stable, display-safe metadata for a registered tool."""

    id: str
    name: str
    description: str
    category_id: str
    version: str = "0.1.0"
    permissions: tuple[str, ...] = ()


class Tool(Protocol):
    """Interface implemented by a tool adapter."""

    @property
    def metadata(self) -> ToolMetadata:
        """Return immutable tool metadata."""

    def execute(
        self,
        context: ToolContext,
        parameters: Mapping[str, object],
    ) -> ToolResult:
        """Execute the tool and return a normalized result."""
