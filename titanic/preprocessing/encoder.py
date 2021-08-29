"""Titanic dataset encoder."""
from typing import List
import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from ..data.titanic import Titanic


class TitanicEncoder:
    """Titanic dataset encoder."""

    enc: OneHotEncoder

    def __init__(self) -> None:
        """Initialize TitanicEncoder."""
        self.enc = OneHotEncoder(handle_unknown="ignore")

    def fit(self, data: List[Titanic]) -> None:
        """Fit the OneHotEncoder based on <data>.

        Args:
            data:   Titanic dataset to fit the encoder on.
        """
        # Extract only categorical variables from <data>, as numerical variables
        # shouldn't be one hot encoded.
        categorical = [
            [
                v.value
                for k, v in row.categorical.__dict__.items()
                if k != "__initialised__"
            ]
            for row in data
        ]

        # Fit the OneHotEncoder using <categorical> data
        self.enc.fit(categorical)

    def encode(self, data: List[Titanic]) -> np.ndarray:
        """Encode <data> using the OneHotEncoder, assuming that it is already fitted.

        This function one hot encodes categorical variables, and normalizes numerical
        variables.

        Args:
            data:   Titanic dataset to encode.

        Returns:
            Numpy array of the encoded Titanic data, to be used for prediction or
            training an ML model.
        """
        # Extract only categorical variables from <data>, as numerical variables
        # shouldn't be one hot encoded.
        categorical = [
            [
                v.value
                for k, v in row.categorical.__dict__.items()
                if k != "__initialised__"
            ]
            for row in data
        ]

        # One hot encode/transform categorical variables
        categorical_enc = self.enc.transform(categorical).toarray()

        # Extract only numerical variables from <data>, as these should be normalized
        numerical = [
            [v for k, v in row.numerical.__dict__.items() if k != "__initialised__"]
            for row in data
        ]

        # Normalize numerical variables
        normalizer = MinMaxScaler()
        numerical_enc = normalizer.fit_transform(numerical)

        # Stack encoded categorical and numerical dimensions next to each other
        data_enc = np.hstack((categorical_enc, numerical_enc))

        return data_enc
