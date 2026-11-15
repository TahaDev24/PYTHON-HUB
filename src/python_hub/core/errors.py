"""Domain-specific exceptions."""


class PythonHubError(Exception):
    """Base exception for expected PYTHON HUB failures."""


class ConfigurationError(PythonHubError):
    """Raised when application configuration is invalid."""


class DuplicateToolError(PythonHubError):
    """Raised when a tool identifier is already registered."""


class ToolNotFoundError(PythonHubError):
    """Raised when a requested tool does not exist in the registry."""
