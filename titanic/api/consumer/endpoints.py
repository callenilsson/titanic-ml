"""API endpoint enums."""
from enum import Enum


class Endpoint(str, Enum):
    """API endpoint enums."""

    GET_TITANIC_DATA = "/endpoint/to/titanic/data"
