"""Train, test, save, and load functions for ML models."""
import os
import shutil
import pickle  # nosec
from typing import List, Tuple, Optional
from datetime import datetime
import dateutil.parser
from sklearn.svm import SVC
from sklearn import metrics
from ..preprocessing.encoder import TitanicEncoder
from ..data.titanic import Titanic

MODEL_PATH = "titanic/ml/models"


def train(x_train: List[Titanic], y_train: List[int]) -> Tuple[SVC, TitanicEncoder]:
    """Fit TitanicEncoder and train ML model using <x_train> and <y_train> data.

    Args:
        x_train:    Titanic dataset to train on.
        y_train:    Titanic survival labels to train on.

    Returns:
        Tuple of the trained SVC model and fitted TitanicEncoder.
    """
    # Create TitanicEncoder to encode categorical data and normalize numerical data
    encoder = TitanicEncoder()
    encoder.fit(x_train)
    x_train_enc = encoder.encode(x_train)

    # Train SVC model
    model = SVC(probability=True)
    model.fit(x_train_enc, y_train)

    return model, encoder


def test(
    x_test: List[Titanic],
    y_test: List[int],
    model: Optional[SVC] = None,
    encoder: Optional[TitanicEncoder] = None,
) -> float:
    """Test ML model on <x_test> and <y_test> data.

    Args:
        x_test:     Titanic dataset to evaluate on.
        y_test:     Titanic survival ground truth labels to use for evaluation.
        model:      Optional ML model, if not provided, the latest stored will be loaded
        encoder:    Optional encoder, if not provided, the latest stored will be loaded.

    Returns:
        Float accuracy score of the model.
    """
    # Load latest saved model & encoder (should be stored in cloud), if not provided
    model, encoder = (
        load_latest() if model is None or encoder is None else (model, encoder)
    )

    # Encode categorical data and normalize numerical data
    x_test_enc = encoder.encode(x_test)

    # Predict data
    y_pred = model.predict(x_test_enc)

    # Accuracy score
    score = round(metrics.accuracy_score(y_pred, y_test), 2)

    return score


def save(model: SVC, encoder: TitanicEncoder) -> None:
    """Save <model> and <encoder> to file, versioned by date.

    Args:
        model:      The ML model to save to file.
        encoder:    The TitanicEncoder to save to file.
    """
    # Create directory for model and encoder
    date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    os.mkdir(f"{MODEL_PATH}/{date}")

    # Save model to file
    model_path = f"{MODEL_PATH}/{date}/model.pkl"
    with open(model_path, "wb") as file:  # nosec
        pickle.dump(model, file)

    # Save encoder to file
    enc_path = f"{MODEL_PATH}/{date}/encoder.pkl"
    with open(enc_path, "wb") as file:  # nosec
        pickle.dump(encoder, file)


def load_latest() -> Tuple[SVC, TitanicEncoder]:
    """Load the latest trained ML model and encoder from file.

    Returns:
        Tuple of the loaded ML model and TitanicEncoder.
    """
    # Get the folder with the latest date
    latest_date = max(
        dateutil.parser.parse(date) for date in os.listdir(f"{MODEL_PATH}/")
    ).strftime("%Y-%m-%dT%H:%M:%S")

    # Load model from file
    model_path = f"{MODEL_PATH}/{latest_date}/model.pkl"
    with open(model_path, "rb") as file:  # nosec
        model = pickle.load(file)

    # Load encoder from file
    enc_path = f"{MODEL_PATH}/{latest_date}/encoder.pkl"
    with open(enc_path, "rb") as file:  # nosec
        encoder = pickle.load(file)

    return model, encoder


def delete_latest() -> None:
    """Delete the latest trained ML model and encoder files."""
    # Get the folder with the latest date
    latest_date = max(
        dateutil.parser.parse(date) for date in os.listdir(f"{MODEL_PATH}/")
    ).strftime("%Y-%m-%dT%H:%M:%S")

    # Remove the folder with the latest date, and its model & encoder files
    shutil.rmtree(f"{MODEL_PATH}/{latest_date}")
