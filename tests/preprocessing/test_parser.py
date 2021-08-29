"""Test Titanic dataset parser."""
import pandas as pd
from titanic.preprocessing import parser


def test_create_titanic_dataset():
    """Verify create_titanic() creates a dataset based on raw a pandas DataFrame."""
    # setup
    train_raw = pd.read_csv("titanic/data/csv/train.csv")

    # when
    train, labels = parser.create_titanic(train_raw)

    # then
    assert isinstance(train, list)
    assert isinstance(labels, list)
    assert len(train) > 0
    assert len(labels) > 0
