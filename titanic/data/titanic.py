"""Titanic dataclasses."""
from pydantic import Field, StrictInt, StrictFloat
from pydantic.dataclasses import dataclass
from .enums import PersonClass, NameTitle, Sex, CabinLetter, Embarked

# Using pydantic to get runtime type checking of all variables. This is very
# important for having good data quality, so all users can trust the data 100%.


@dataclass
class Categorical:
    """Categorical variables of the Titanic dataset."""

    person_class: PersonClass
    name_title: NameTitle
    sex: Sex
    cabin_letter: CabinLetter
    embarked: Embarked


@dataclass
class Numerical:
    """Numerical variables of the Titanic dataset."""

    age: StrictFloat = Field(..., example=30.5)
    siblings_spouses: StrictInt = Field(..., example=3)
    parents_children: StrictInt = Field(..., example=2)
    cabin_number: StrictInt = Field(..., example=53)
    ticket_price: StrictFloat = Field(..., example=27.2)


@dataclass
class Titanic:
    """Titanic dataset dataclass."""

    categorical: Categorical
    numerical: Numerical
