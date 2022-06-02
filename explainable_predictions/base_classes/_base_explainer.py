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

    def __init__(self, objective: Optional[str] = 'regression') -> None:
        """_summary_

        Args:
            objective (str, optional): Objective of your model. Options: 'regression' or 'classification' Defaults to 'regression'.
        """
        self.objective = objective
        self.model = None
        self.explainer = None
        

        # Forces random seed, so all methods that use it are replicable

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
    
    