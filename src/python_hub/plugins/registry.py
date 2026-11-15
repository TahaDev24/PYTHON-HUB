"""In-process registry for explicitly loaded tool adapters."""

from __future__ import annotations

from collections.abc import Iterable

from python_hub.core.errors import DuplicateToolError, ToolNotFoundError
from python_hub.plugins.contracts import Tool


class ToolRegistry:
    """Store tool adapters by stable identifier.

    This registry is not a sandbox, installer, package resolver, or trust boundary.
    """

    def __init__(self) -> None:
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        """Register a tool, rejecting duplicate identifiers."""
        tool_id = tool.metadata.id.strip()
        if not tool_id:
            raise ValueError("tool metadata id cannot be empty")
        if tool_id in self._tools:
            raise DuplicateToolError(f"tool '{tool_id}' is already registered")
        self._tools[tool_id] = tool

    def get(self, tool_id: str) -> Tool:
        """Return a registered tool or raise a domain-specific error."""
        try:
            return self._tools[tool_id]
        except KeyError as exc:
            raise ToolNotFoundError(f"tool '{tool_id}' is not registered") from exc

    def list(self) -> tuple[Tool, ...]:
        """Return registered tools in registration order."""
        return tuple(self._tools.values())

    def ids(self) -> tuple[str, ...]:
        """Return registered tool identifiers."""
        return tuple(self._tools)

    def register_many(self, tools: Iterable[Tool]) -> None:
        """Register multiple tools atomically."""
        original = self._tools.copy()
        try:
            for tool in tools:
                self.register(tool)
        except Exception:
            self._tools = original
            raise
