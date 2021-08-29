"""API connector class to request/put data from/to various APIs."""
from typing import Optional, Union, Tuple, Any
from .endpoints import Endpoint


class APIConnector:
    """API connector class to request/put data from/to various APIs."""

    client_id: str
    client_secret: str
    base_url: str
    api: Any

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        base_url: Optional[str] = None,
    ) -> None:
        """Set up connection to an API.

        Args:
            client_id:       Client id to connect with.
            client_secret:   Client secret to connect with.
            base_url:        Base URL of the API to connect to.
        """
        # <Code here to connect to an API>

    def get(self, endpoint: Union[Endpoint, str]) -> Tuple[Any, bool]:
        """Get data from an API according to <endpoint>.

        Args:
            endpoint:   The endpoint to get data from.

        Returns:
            Tuple of JSON response data and an OK boolean.
        """
        # <Code here to get data from an API>

    def put(self, endpoint: Endpoint, data: Any) -> bool:
        """Put <data> to an API according to <endpoint>.

        Args:
            endpoint:    The endpoint to put data to.
            data:        JSON data to put to the API.
        Returns:
            OK boolean.
        """
        # <Code here to put data to an API>
