# pylint: disable-all

import unittest
import os
from flask_option import start

class TestFlaskOption(unittest.TestCase):
    def test_start_with_flask_env_development(self):
        os.environ['FLASK_ENV'] = 'development'
        self.assertEqual(start(), "Starting in development mode...")

    def test_start_with_flask_env_production(self):
        os.environ['FLASK_ENV'] = 'production'
        self.assertEqual(start(), "Starting in production mode...")

    def test_start_with_no_flask_env(self):
        del os.environ['FLASK_ENV']
        try:
            start()
        except KeyError:
            self.fail("Your program should be able to run without a FLASK_ENV variable defined")
        self.assertEqual(start(), "Starting in empty mode...")
