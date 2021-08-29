"""Test Titanic dataclasses."""
import pytest
from pydantic.error_wrappers import ValidationError
from titanic.data.titanic import Categorical, Numerical


def test_invalid_data_types():
    """Verify dataclasses cannot be created with wrong data types."""
    # when
    with pytest.raises(ValidationError):
        Categorical(32, None, True, 15.2, "random_string")

    with pytest.raises(ValidationError):
        Numerical(32, 12.5, None, True, "random_string")
