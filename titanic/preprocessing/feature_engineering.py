"""Feature engineering functions."""
import re
import numpy as np
import pandas as pd
from ..data.enums import CabinLetter, ColumnsProcessed


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """Feature engineer / extract new features from from Titanic <df>.

    Args:
        df: DataFrame to feature engineer new features to.

    Returns:
        The updated DataFrame with new featured engineered columns.
    """
    # Extract name titles
    df = extract_name_title(df)

    # Extract cabin letters and cabin numbers
    df = extract_cabin_letter_number(df)

    return df


def extract_name_title(df: pd.DataFrame) -> pd.DataFrame:
    """Extract name titles from the name column, and put into a new column.

    Args:
        df: DataFrame to extract name titles from, and append to a new column.

    Returns:
        The updated DataFrame with a new name title column.
    """
    # Extract name titles for each name, and put them into a new "name_title" column
    df[ColumnsProcessed.NAME_TITLE.value] = [
        name.split(",")[1].split(".")[0].strip()
        for name in df[ColumnsProcessed.NAME.value]
    ]
    return df


def extract_cabin_letter_number(df: pd.DataFrame) -> pd.DataFrame:
    """Extract cabin letters & numbers from the cabin column, and put into a new column.

    Args:
        df: DataFrame to extract cabin letters & numbers from, and append to new columns

    Returns:
        The updated DataFrame with new cabin letter and cabin number columns.
    """
    # Clean cabins with multiple cabin names in one, as that makes no sense (noise).
    # Instead keep only the first cabin name if it is a multiple.
    # Example "C23 C25 C27" -> "C23"
    cabins_clean = [
        cabin.split(" ")[0] if isinstance(cabin, str) else cabin
        for cabin in df[ColumnsProcessed.CABIN.value]
    ]

    # Extract cabin letters and numbers from "cabin" column
    cabin_letters = [
        "".join(re.findall("[A-Z]+", cabin)) if isinstance(cabin, str) else cabin
        for cabin in cabins_clean
    ]
    cabin_numbers = [
        "".join(re.findall("[0-9]+", cabin)) if isinstance(cabin, str) else cabin
        for cabin in cabins_clean
    ]

    # Set NaN cabin letters & empty strings as "none"
    cabin_letters = [
        letter
        if isinstance(letter, str) and len(letter) > 0
        else CabinLetter.NONE.value
        for letter in cabin_letters
    ]

    # Convert cabin number strings to integers, or np.nan if NaN/None
    cabin_numbers = [
        int(number) if isinstance(number, str) and len(number) > 0 else np.nan
        for number in cabin_numbers
    ]

    # Add new columns to dataframe
    df[ColumnsProcessed.CABIN_LETTER.value] = cabin_letters
    df[ColumnsProcessed.CABIN_NUMBER.value] = np.array(cabin_numbers).astype(int)

    return df
