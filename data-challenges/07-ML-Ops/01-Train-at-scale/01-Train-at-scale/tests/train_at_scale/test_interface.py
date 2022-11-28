from unittest.mock import patch

from tests.test_base import TestBase

import numpy as np
import pandas as pd

# Override DATASET_SIZE just for this test to speed up results
@patch("taxifare.ml_logic.params.DATASET_SIZE", new="1k")
@patch("taxifare.ml_logic.params.VALIDATION_DATASET_SIZE", new="1k")
@patch("taxifare.ml_logic.params.CHUNK_SIZE", new=200)
class TestInterface(TestBase):
    """Assert that code logic run and output the correct type.
    Do not check model performance
    """

    def test_route_preprocess_and_train(self):

        from taxifare.interface.main_local import preprocess_and_train

        # Call preprocess_and_train() to check if code pass and store related pickle
        preprocess_and_train()

        # Test newly created pickle
        results = self.load_results("test_preprocess_and_train", extension=".pickle")
        mae = results["metrics"]["mae"]
        assert isinstance(mae, float), "preprocess_and_train() should store mae as float"

    def test_route_pred(self):

        from taxifare.interface.main_local import pred

        # Call pred() to check if code pass and store pickle
        pred()

        # Test newly created pickle
        results = self.load_results("test_pred", extension=".pickle")
        y_pred = results["y_pred"].flat[0].tolist()
        assert isinstance(y_pred, float), "calling pred() should return a float"

    def test_route_preprocess(self):

        from taxifare.interface.main_local import preprocess

        # Call preprocess() to check if code pass, and store corresponding pickle
        preprocess()

        # Test newly created pickle
        results = self.load_results("test_preprocess", extension=".pickle")
        data_processed_head = results["data_processed_head"]
        truth = pd.read_csv("https://storage.googleapis.com/datascience-mlops/taxi-fare-ny/processed/train_processed_1k.csv", header=None, skiprows=1, dtype=np.float32).to_numpy()[0:10]
        assert data_processed_head.shape[1] == truth.shape[1], "You created an incorrect number of columns after preprocessing. There should be 66 (65 features data_processed + 1 target)"
        assert np.allclose(data_processed_head[0], truth[0], atol=1e-3), "First row differs. Did you store headers in your CSV by mistake?"
        assert np.allclose(truth, data_processed_head, atol=1e-3), "One of your data processed value is somehow incorrect!"

    def test_route_train(self):

        from taxifare.interface.main_local import train

        train()
