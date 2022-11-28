import nbresult
import pandas as pd
import numpy as np
from nbresult import ChallengeResultTestCase


class TestPipe(ChallengeResultTestCase):

    def test_pipe_not_crashing(self):
        self.assertTrue(self.result.shape, (1000, 32))
