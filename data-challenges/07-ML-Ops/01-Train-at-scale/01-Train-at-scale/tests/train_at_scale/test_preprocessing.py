import pytest
import numpy as np
import os

TEST_ENV = os.getenv("TEST_ENV")


def test_preprocess_features(train_1k_cleaned, X_processed_1k):
    from taxifare.ml_logic.preprocessor import preprocess_features
    res = preprocess_features(train_1k_cleaned)
    assert res.shape == X_processed_1k.shape
    assert np.allclose(res, X_processed_1k)
