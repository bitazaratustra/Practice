from tests.test_base import TestBase

import os
import numpy as np
import pytest

from google.cloud import bigquery


TEST_ENV = os.getenv("TEST_ENV")


class TestCloudData(TestBase):
    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_big_query_dataset_variable_exists(self):
        """
        Verify the DATASET variable is set
        """
        dataset = os.environ.get('DATASET')

        assert dataset is not None

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_cloud_data_create_dataset(self):
        """
        verify that the bq dataset is created and the Makefile variable correct
        """
        dataset = os.environ.get('DATASET')
        if dataset is None:
            raise ValueError("The DATASET environment variable is not set")
        client = bigquery.Client()
        datasets = [dataset.dataset_id for dataset in client.list_datasets()]

        assert dataset in datasets, f"Dataset {dataset} does not exist on the active GCP project"

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_cloud_data_create_table(self):
        """
        verify that the bq dataset tables are created and the Makefile variables correct
        """
        expected_tables = ["train_10k", "val_10k"]
        dataset = os.environ.get('DATASET')
        if dataset is None:
            raise ValueError("The DATASET environment variable is not set")
        client = bigquery.Client()
        tables = [table.table_id for table in client.list_tables(dataset)]
        for table in expected_tables:
            assert table in tables, f"Table {table} is missing from the {dataset} dataset"

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_cloud_data_table_content(self):
        """
        verify the format of the created bq tables
        """
        expected_tables = ["train_10k", "val_10k"]
        parameters = {
            'columns':
                {
                    'key': 'timestamp',
                    'fare_amount': 'float',
                    'pickup_datetime': 'timestamp',
                    'pickup_longitude': 'float',
                    'pickup_latitude': 'float',
                    'dropoff_longitude': 'float',
                    'dropoff_latitude': 'float',
                    'passenger_count': 'integer'
                },
            'n_rows': 10000
        }
        project = os.environ.get('PROJECT')
        dataset = os.environ.get('DATASET')
        if dataset is None:
            raise ValueError("The DATASET environment variable is not set")
        client = bigquery.Client()
        for table_id in expected_tables:
            table_id = f'{project}.{dataset}.{table_id}'
            table = client.get_table(table_id)
            columns = {}
            for column in table.schema:
                columns[column.name] = column.field_type.lower()
            assert columns == parameters['columns']
            assert table.num_rows == parameters['n_rows']

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_cloud_data_bq_chunks(self):
        """
        verify the value of the `fare_amount` column for the first 10 observations of the training dataset table
        """
        from taxifare.data_sources.big_query import get_bq_chunk
        from taxifare.ml_logic.params import DTYPES_RAW_OPTIMIZED

        training_rows = get_bq_chunk("train_10k", 0, 10, DTYPES_RAW_OPTIMIZED)
        fare_amount = list(training_rows.fare_amount)
        fare_amount = [round(f, 1) for f in fare_amount]

        # validate data types
        dtypes = training_rows.dtypes

        for column, data_type in DTYPES_RAW_OPTIMIZED.items():

            returned_data_type = dtypes[column]

            if data_type == "O":
                expected_data_type = object
            elif data_type == "float32":
                expected_data_type = np.float32
            elif data_type == "int8":
                expected_data_type = np.int8

            assert returned_data_type == expected_data_type, f"The column {column} is expected to contain the type {data_type}"
