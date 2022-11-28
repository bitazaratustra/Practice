import numpy as np
import pandas as pd
import os

from tests.test_base import write_result

from taxifare.ml_logic.data import clean_data
from taxifare.ml_logic.model import initialize_model, compile_model, train_model
from taxifare.ml_logic.preprocessor import preprocess_features
from taxifare.ml_logic.registry import save_model, load_model

from taxifare.ml_logic.params import (
    CHUNK_SIZE,
    DTYPES_RAW_OPTIMIZED_HEADLESS,
    DTYPES_RAW_OPTIMIZED,
    DTYPES_PROCESSED_OPTIMIZED,
    COLUMN_NAMES_RAW,
    DATASET_SIZE,
    VALIDATION_DATASET_SIZE,
    LOCAL_DATA_PATH
)


def preprocess_and_train():
    """
    Load historical data in memory, clean and preprocess it, train a Keras model on it,
    save the model, and finally compute & save a performance metric
    on a validation set holdout at the `model.fit()` level
    """

    print("\n⭐️ Use case: preprocess and train basic")


    # Retrieve raw data
    data_raw_path = os.path.join(LOCAL_DATA_PATH, "raw", f"train_{DATASET_SIZE}.csv")
    data = pd.read_csv(data_raw_path, dtype=DTYPES_RAW_OPTIMIZED)

    # Clean data using ml_logic.data.clean_data
    # YOUR CODE HERE

    # Create X, y
    # YOUR CODE HERE

    # Preprocess X using `preprocessor.py`
    # YOUR CODE HERE

    # Train model on X_processed and y, using `model.py`
    model = None
    learning_rate = 0.001
    batch_size = 256
    patience = 2

    # YOUR CODE HERE

    # Compute the validation metric (min val mae of the holdout set)
    metrics = dict(mae=np.min(history.history['val_mae']))

    # Save trained model
    params = dict(
        learning_rate=learning_rate,
        batch_size=batch_size,
        patience=patience
    )

    save_model(model, params=params, metrics=metrics)

    # 🧪 Write outputs so that they can be tested by make test_train_at_scale (do not remove)
    write_result(name="test_preprocess_and_train", subdir="train_at_scale", metrics=metrics)

    print("✅ preprocess_and_train() done")


def pred(X_pred: pd.DataFrame = None) -> np.ndarray:

    if X_pred is None:
        X_pred = pd.DataFrame(dict(
            key=["2013-07-06 17:18:00"],  # useless but the pipeline requires it
            pickup_datetime=["2013-07-06 17:18:00 UTC"],
            pickup_longitude=[-73.950655],
            pickup_latitude=[40.783282],
            dropoff_longitude=[-73.984365],
            dropoff_latitude=[40.769802],
            passenger_count=[1]
        ))

    model = load_model()

    # Preprocess the new data
    # YOUR CODE HERE

    # Make a prediction
    # YOUR CODE HERE

    # 🧪 Write outputs so that they can be tested by make test_train_at_scale (do not remove)
    write_result(name="test_pred", subdir="train_at_scale", y_pred=y_pred)
    print("✅ prediction done: ", y_pred, y_pred.shape)

    return y_pred


if __name__ == '__main__':
    try:
        preprocess_and_train()
        pred()
    except:
        import ipdb, traceback, sys
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
