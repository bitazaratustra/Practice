from tests.test_base import TestBase

import os
import pytest
from google.cloud import storage


TEST_ENV = os.getenv("TEST_ENV")


class TestGcpSetup(TestBase):
    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_setup_key_env(self):
        """
        verify that `$GOOGLE_APPLICATION_CREDENTIALS` is defined
        """

        # verify env var presence
        assert os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), "GCP environment variable not defined"

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_setup_key_path(self):
        """
        verify that `$GOOGLE_APPLICATION_CREDENTIALS` points to an existing file
        """

        service_account_key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

        # verify env var path existence
        with open(service_account_key_path, "r") as file:
            content = file.read()

        assert content is not None

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_code_get_project(self):
        """
        retrieve default gcp project id with code
        """
        # get default project id
        client = storage.Client()
        project_id = client.project

        assert project_id is not None

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_setup_project_id(self):
        """
        verify that the provided project id is correct
        """
        env_project_id = os.environ.get('PROJECT')
        # get default project id
        client = storage.Client()
        project_id = client.project

        assert env_project_id == project_id, f"PROJECT environmental variable differs from the activated GCP project ID"

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_setup_bucket_exists(self):
        """
        verify that buckets exist
        """
        client = storage.Client()
        buckets = [bucket.name for bucket in client.list_buckets()]

        assert len(buckets) > 0, "no buckets found"

    @pytest.mark.skipif(TEST_ENV != "development", reason="only dev mode")
    def test_setup_bucket_name(self):
        """
        verify that the provided bucket name is correct
        """

        env_bucket_name = os.environ.get('BUCKET_NAME')
        client = storage.Client()
        buckets = [bucket.name for bucket in client.list_buckets()]

        assert env_bucket_name in buckets, f"Bucket {env_bucket_name} does not exist in your GCP project"
        assert "/" not in env_bucket_name
        assert ":" not in env_bucket_name
