"""Test Titanic ML model functions."""
import pandas as pd
from titanic.ml import model
from titanic.preprocessing import parser


def test_model_train_and_test():
    """Verify train() and test() trains and tests an ML model."""
    # setup
    train_raw = pd.read_csv("titanic/data/csv/train.csv")
    x_train, y_train = parser.create_titanic(train_raw)

    # when
    model_, encoder = model.train(x_train, y_train)
    score = model.test(x_train, y_train, model_, encoder)

    # then
    assert score > 0.0


def test_model_save_load_and_delete():
    """Verify save, load and delete functions saves, loads and deletes ML models."""
    # setup
    train_raw = pd.read_csv("titanic/data/csv/train.csv")
    # Create dataset from raw data
    x_train, y_train = parser.create_titanic(train_raw)
    # Train model and fit encoder
    model_, encoder = model.train(x_train, y_train)

    # when
    # Save model and encoder to file
    model.save(model_, encoder)
    # Load model and encoder to file
    model_load, encoder_load = model.load_latest()
    # Test loaded model and encoder
    score = model.test(x_train, y_train, model_load, encoder_load)
    # Delete latest model and encoder
    model.delete_latest()

    # then
    assert score > 0.0
