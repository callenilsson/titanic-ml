"""Test TitanicEncoder."""
import pandas as pd
from titanic.preprocessing.encoder import TitanicEncoder
from titanic.preprocessing import parser


def test_fit_encoder():
    """Verify TitanicEncoder encodes the Titanic dataset."""
    # setup
    enc = TitanicEncoder()
    data_raw = pd.read_csv("titanic/data/csv/train.csv")
    data, labels = parser.create_titanic(data_raw)  # pylint: disable=unused-variable

    # when
    enc.fit(data)
    data_enc = enc.encode(data)

    # then
    assert data_enc.shape[0] == len(data)
    assert data_enc.shape[1] == 39
