import pytest
import numpy as np
import os

TEST_ENV = os.getenv("TEST_ENV")


def test_model_architecture_and_fit(X_processed_1k, y_1k):

    from taxifare.ml_logic.model import initialize_model,compile_model, train_model

    model = initialize_model(X_processed_1k)
    trainable_params = np.sum([np.prod(v.get_shape()) for v in model.trainable_weights])

    expected = 12621
    assert trainable_params == expected, "Your model architecture does not match that of the notebook"

    model = compile_model(model, learning_rate=0.001)

    model, history = train_model(model=model,
                                 X=X_processed_1k,
                                 y=y_1k,
                                 batch_size=256,
                                 validation_split=0.3)

    assert min(history.history['loss']) < 220, "Your model does not seem to fit correctly"
