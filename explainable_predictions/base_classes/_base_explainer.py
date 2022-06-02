"""
This module contais the interface fot the encapsulation of all predictive models.
"""

from abc import abstractmethod, ABC
import pandas as pd
import numpy as np
from typing import Optional

__all__ = ["BaseExplainer"]


## TODO: Document this class
## TODO: Set base parameters

class BaseExplainer(ABC):
    """Base class for encapsulation of all predictive models"""

    def __init__(
        self,
        target_col: str,
        features_cols: list = None,
        categorical_features_cols: list = None,
        col_dtypes: dict = None,
        random_seed: int = 42,
    ):
        

        # Forces random seed, so all methods that use it are replicable
        np.random.seed(random_seed)

    @abstractmethod
    def fit(self, X: pd.DataFrame, y: pd.Series):
        """_summary_

        Args:
            X (pd.DataFrame): _description_
            y (pd.Series): _description_
        """
        pass

    @abstractmethod
    def predict():
        pass

    @abstractmethod
    def explain_model(model, explain_values):
        pass

    @abstractmethod
    def _fit_model():
        pass

    @abstractmethod
    def _fit_explainer():
        pass

    @abstractmethod
    def _predict_explainer():
        pass
    
    