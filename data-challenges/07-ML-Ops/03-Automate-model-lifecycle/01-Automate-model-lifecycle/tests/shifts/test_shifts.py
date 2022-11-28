import os
import pytest

from tests.test_base import TestBase

MLFLOW_DB_USER = 'taxifare_readonly'
MLFLOW_DB_PASSWORD = 'm4e7dbNPDPg8tNR2Br36NgUGd3'
MLFLOW_DB_HOSTNAME = 'wagon-mlflo-1768.postgresql.a.osc-fr1.scalingo-dbs.com'
MLFLOW_DB_PORT = '37750'
MLFLOW_DB_NAME = 'wagon_mlflo_1768'
MLFLOW_TRACKING_DB_URL = f"postgresql://{MLFLOW_DB_USER}:{MLFLOW_DB_PASSWORD}@{MLFLOW_DB_HOSTNAME}:{MLFLOW_DB_PORT}/{MLFLOW_DB_NAME}"

TEST_ENV = os.environ.get('TEST_ENV')

class TestShifts(TestBase):

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_mlflow_db_user(self):
        """
        verify that the shifts parameters are correctly set
        """
        db_user = os.environ.get('MLFLOW_DB_USER')
        assert db_user == MLFLOW_DB_USER

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_mlflow_db_password(self):
        """
        verify that the shifts parameters are correctly set
        """
        db_password = os.environ.get('MLFLOW_DB_PASSWORD')
        assert db_password == MLFLOW_DB_PASSWORD

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_mlflow_db_hostname(self):
        """
        verify that the shifts parameters are correctly set
        """
        db_hostname = os.environ.get('MLFLOW_DB_HOSTNAME')
        assert db_hostname == MLFLOW_DB_HOSTNAME

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_mlflow_db_port(self):
        """
        verify that the shifts parameters are correctly set
        """
        db_port = os.environ.get('MLFLOW_DB_PORT')
        assert db_port == MLFLOW_DB_PORT

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_mlflow_db_name(self):
        """
        verify that the shifts parameters are correctly set
        """
        db_name = os.environ.get('MLFLOW_DB_NAME')
        assert db_name == MLFLOW_DB_NAME

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_mlflow_db_url(self):
        """
        verify that the shifts parameters are correctly set
        """
        db_url = os.environ.get('MLFLOW_TRACKING_DB')
        assert db_url == MLFLOW_TRACKING_DB_URL

    def test_shifts_get_next_first_row_value(self):
        """
        verify the retrieval of the latest trained row
        """
        from taxifare.ml_logic.registry_db import get_next_first_row

        experiment = 'taxifare_experiment_recap'
        next_row = get_next_first_row(experiment)
        assert next_row == 10000

    def test_shifts_get_next_first_row_is_int(self):
        """
        verify the retrieval of the latest trained row
        """
        from taxifare.ml_logic.registry_db import get_next_first_row

        experiment = 'taxifare_experiment_recap'
        next_row = get_next_first_row(experiment)
        assert isinstance(next_row, int)

    def test_shifts_complete(self):
        """
        verify that the complete workflow runs on all new data chunks
        """

        # TODO
        assert True
