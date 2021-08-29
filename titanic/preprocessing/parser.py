"""Titanic dataset parse functions."""
from typing import List, Dict, Any, Tuple
import pandas as pd
from .feature_engineering import feature_engineering
from ..data.enums import (
    PersonClass,
    NameTitle,
    Sex,
    CabinLetter,
    Embarked,
    ColumnsRaw,
    ColumnsProcessed,
)
from ..data.titanic import Titanic, Categorical, Numerical

# Dict of which column names to rename to be more understandable
RENAME_COLUMNS = {
    ColumnsRaw.PASSENGER_ID.value: ColumnsProcessed.PASSENGER_ID.value,
    ColumnsRaw.SURVIVED.value: ColumnsProcessed.SURVIVED.value,
    ColumnsRaw.PERSON_CLASS.value: ColumnsProcessed.PERSON_CLASS.value,
    ColumnsRaw.NAME.value: ColumnsProcessed.NAME.value,
    ColumnsRaw.SEX.value: ColumnsProcessed.SEX.value,
    ColumnsRaw.AGE.value: ColumnsProcessed.AGE.value,
    ColumnsRaw.SIBLINGS_SPOUSES.value: ColumnsProcessed.SIBLINGS_SPOUSES.value,
    ColumnsRaw.PARENTS_CHILDREN.value: ColumnsProcessed.PARENTS_CHILDREN.value,
    ColumnsRaw.TICKET.value: ColumnsProcessed.TICKET.value,
    ColumnsRaw.CABIN.value: ColumnsProcessed.CABIN.value,
    ColumnsRaw.EMBARKED.value: ColumnsProcessed.EMBARKED.value,
    ColumnsRaw.TICKET_PRICE.value: ColumnsProcessed.TICKET_PRICE.value,
}

# Dict of which values to rename to be more understandable
RENAME_VALUES: Dict[ColumnsProcessed, Dict[Any, Any]] = {
    ColumnsProcessed.PERSON_CLASS: {
        1: PersonClass.UPPER,
        2: PersonClass.MIDDLE,
        3: PersonClass.LOWER,
    },
    ColumnsProcessed.EMBARKED: {
        "C": Embarked.CHERBOURG,
        "Q": Embarked.QUEENSTOWN,
        "S": Embarked.SOUTHAMPTON,
    },
}


def create_titanic(df: pd.DataFrame) -> Tuple[List[Titanic], List[int]]:
    """Create Titanic dataset based on raw <df> data.

    Args:
        df: The raw Titanic dataset DataFrame.

    Returns:
        Tuple of the parsed Titanic dataset and y labels.
    """
    # Rename columns to be more understandable
    df = df.rename(columns=RENAME_COLUMNS)

    # Rename values to be more understandable
    for col, rename in RENAME_VALUES.items():
        for from_, to in rename.items():
            df.loc[df[col.value] == from_, col.value] = to.value

    # Extract and add more features (feature engineering)
    df = feature_engineering(df)

    # Clean data from NaN/None values
    df = clean(df)

    # Create list of Titanic objects from <df>
    data = [
        Titanic(
            categorical=Categorical(
                person_class=PersonClass(row[ColumnsProcessed.PERSON_CLASS.value]),
                name_title=NameTitle(row[ColumnsProcessed.NAME_TITLE.value]),
                sex=Sex(row[ColumnsProcessed.SEX.value]),
                cabin_letter=CabinLetter(row[ColumnsProcessed.CABIN_LETTER.value]),
                embarked=Embarked(row[ColumnsProcessed.EMBARKED.value]),
            ),
            numerical=Numerical(
                age=row[ColumnsProcessed.AGE.value],
                siblings_spouses=row[ColumnsProcessed.SIBLINGS_SPOUSES.value],
                parents_children=row[ColumnsProcessed.PARENTS_CHILDREN.value],
                cabin_number=row[ColumnsProcessed.CABIN_NUMBER.value],
                ticket_price=row[ColumnsProcessed.TICKET_PRICE.value],
            ),
        )
        for _, row in df.iterrows()
    ]

    # Get labels from <df>
    labels = list(df[ColumnsProcessed.SURVIVED.value].to_numpy().astype(int))

    return data, labels


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Clean <df> from NaN/None values.

    All rows that has a NaN/None categorical variable are dropped.
    All rows that has a NaN/None numerical variable are filled with the average of the
    column to forcefully make the data continuous.

    Args:
        df: DataFrame to clean from NaN/None values.

    Returns:
        The new cleaned DataFrame without any NaN/None values.
    """
    # For all Categorical variables, drop all rows that are NaN/None
    for col in Categorical.__annotations__:  # pylint: disable=no-member
        df = df.dropna(subset=[col])

    # For all Numerical variables, replace NaN/None values with the column average to
    # forcefully make the data continuous
    for col in Numerical.__annotations__:  # pylint: disable=no-member
        df[col] = df[col].fillna(df[col].mean())

    return df
