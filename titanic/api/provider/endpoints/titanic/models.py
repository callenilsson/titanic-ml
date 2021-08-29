"""Titanic schema models."""
from pydantic import BaseModel, Field, StrictFloat


class SurvivalPrediction(BaseModel):
    """Titanic survival prediction for a person."""

    survived: StrictFloat = Field(
        ...,
        description="Float prediction of how likely the person would survive Titanic.",
        example=0.78,
    )
