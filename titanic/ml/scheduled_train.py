"""Scheduled cloud function to regularly train & save new ML model versions."""
import pandas as pd
from . import model
from ..preprocessing import parser


def main() -> None:
    """Main function to train & save a new ML model and encoder."""
    # Load data to train from (could be replaced with API consumer)
    train_raw = pd.read_csv("titanic/data/csv/train.csv")

    # Parse, preprocess and verify raw data is correct
    x_train, y_train = parser.create_titanic(train_raw)

    # Train model and fit encoder to the data
    model_, encoder = model.train(x_train, y_train)

    # Test model on training data
    score = model.test(x_train, y_train, model_, encoder)
    print("Accuracy:", score)

    # Save model and encoder to file (should be cloud)
    model.save(model_, encoder)


if __name__ == "__main__":
    main()
