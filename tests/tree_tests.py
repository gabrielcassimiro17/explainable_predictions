import explainable_predictions
from explainable_predictions.exp_trees import RandomForestExplainer
import unittest
import pandas as pd
import numpy as np


class TestTrees(unittest.TestCase):
    def setUp(self):
        """Builds the environment for testing"""

        self.data = pd.DataFrame(
            {"X": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "y": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
        )
        self.model = RandomForestExplainer().fit(self.data[["X"]], self.data[["y"]])

    def test_fit(self):
        """Tests:
        1) If the predictions come in a np.ndarray type
        """

        model = self.model

        self.assertIsInstance(
            model, explainable_predictions.exp_trees.RandomForestExplainer
        )

        return self

    def test_predict(self):
        """Tests:
        1) If the predictions come in a np.ndarray type
        """

        pred, shap_values = self.model.predict(
            self.data[["X"]], graphical_explanation=False
        )

        self.assertIsInstance(pred, np.ndarray)
        self.assertIsNotNone(shap_values)

    # def test_explain_model(self):
    #     """ Tests:
    #             1) If the predictions come in a np.ndarray type
    #     """

    #     pred = self.reg.predict()

    #     self.assertIsInstance(pred, np.ndarray)
