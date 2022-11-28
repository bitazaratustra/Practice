from tests.test_base import TestBase

import os
import pytest

TEST_ENV = os.getenv("TEST_ENV")

class TestPrefect(TestBase):

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_prefect_flow_name_is_not_null(self):
        """
        verify that the prefect parameters are correctly set
        """
        flow_name = os.environ.get('PREFECT_FLOW_NAME')
        assert flow_name is not None, 'PREFECT_FLOW_NAME variable is not defined'

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_prefect_log_level_is_warning(self):
        """
        verify that the prefect parameters are correctly set
        """
        log_level = os.environ.get('PREFECT_LOG_LEVEL')
        assert log_level == 'WARNING'

    def test_prefect_flow(self):
        """
        test complete workflow lifecycle
        """

        flow = self.load_results()

        assert "Flow run SUCCESS: all reference tasks succeeded" in flow


def write_prefect_flow():

    from taxifare.flow import build_flow

    import os

    flow = build_flow()

    mlflow_experiment = os.environ.get("MLFLOW_EXPERIMENT")

    flow.run(parameters=dict(
        experiment=mlflow_experiment))
