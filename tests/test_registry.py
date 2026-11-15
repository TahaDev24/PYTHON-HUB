import pytest

from python_hub.core.errors import DuplicateToolError, ToolNotFoundError
from python_hub.plugins.contracts import ToolMetadata, ToolResult
from python_hub.plugins.registry import ToolRegistry


class ExampleTool:
    metadata = ToolMetadata(
        id="example.echo",
        name="Example Echo",
        description="A test adapter.",
        category_id="automation",
    )

    def execute(self, context, parameters):
        return ToolResult(success=True, message="ok")


def test_register_and_get_tool() -> None:
    registry = ToolRegistry()
    tool = ExampleTool()
    registry.register(tool)
    assert registry.get("example.echo") is tool
    assert registry.ids() == ("example.echo",)


def test_duplicate_tool_is_rejected() -> None:
    registry = ToolRegistry()
    registry.register(ExampleTool())
    with pytest.raises(DuplicateToolError):
        registry.register(ExampleTool())


def test_missing_tool_raises_domain_error() -> None:
    with pytest.raises(ToolNotFoundError):
        ToolRegistry().get("missing.tool")


def test_register_many_is_atomic() -> None:
    registry = ToolRegistry()
    registry.register(ExampleTool())

    class AnotherTool(ExampleTool):
        metadata = ToolMetadata(
            id="example.another",
            name="Another",
            description="Another test adapter.",
            category_id="automation",
        )

    with pytest.raises(DuplicateToolError):
        registry.register_many([AnotherTool(), ExampleTool()])
    assert registry.ids() == ("example.echo",)
