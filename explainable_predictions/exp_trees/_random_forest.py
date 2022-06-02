from typing import Optional
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from explainable_predictions.base_classes import BaseExplainer
import pandas as pd
import shap
import tqdm
import matplotlib.pyplot as plt


__all__ = ["RandomForestExplainer"]

class RandomForestExplainer(BaseExplainer):
    def __init__(self, objective:Optional[str] = 'regression') -> None:
        """_summary_

        Args:
            objective (str, optional): Objective of your model. Options: 'regression' or 'classification' Defaults to 'regression'.
        """
        self.objective = objective
        self.model = None
        self.explainer = None

    
    def fit(self, X: pd.DataFrame, y: pd.Series, params: Optional[dict] = None):
        """_summary_

        Args:
            X (pd.DataFrame): _description_
            y (pd.Series): _description_
        """
        model = self._fit_model(X, y)
        explainer = self._fit_explainer(model)
        
        self.model = model
        self.explainer = explainer

        return self

    
    def predict(self, X: pd.DataFrame, graphical_explanation: bool = True):
        
        
        if self.model == None:
            raise ValueError('Model not fitted. Call fit() first.')

        prediction = self.model.predict(X)
        shap_values = self._predict_explainer(X, graphical_explanation)

        return prediction, shap_values
        

    
    def explain_model(self, model, explain_values):
        """_summary_

        Args:
            model (_type_): _description_
            explain_values (_type_): _description_
        """

        shap.plots.beeswarm(self.explainer(explain_values))
        plt.show()

    
    def _fit_model(self, X: pd.DataFrame, y: pd.Series, params: Optional[dict] = None):
        """_summary_

        Args:
            X (pd.DataFrame): _description_
            y (pd.Series): _description_

        Raises:
            ValueError: _description_
        """
        if self.objective == 'regression':
            model = RandomForestRegressor()
            model.fit(X, y)
            
            return model


        elif self.objective == 'classification':
            model = RandomForestClassifier()
            model.fit(X, y)
            
            return model
        else:
            raise ValueError(f'Objective {self.objective} not supported. \n Supported objectives: "regression" or "classification"')
    
    def _fit_explainer(self, model):
        """_summary_

        Args:
            model (_type_): _description_
        """
        return shap.Explainer(model)


    
    def _predict_explainer(self, X, graphical_explanation: bool = True):
        """_summary_

        Args:
            X (_type_): _description_
            graphical_explanation (bool, optional): _description_. Defaults to True.

        Returns:
            _type_: _description_
        """
        if len(X) > 10:
            print('This may take a while beacause of the amount of data in the prediction')
        
        if graphical_explanation:
            for i in tqdm.tqdm(range(len(X))):
                shap_values = self.explainer(X.iloc[i])
                shap.force_plot(self.explainer.expected_value, shap_values.values,  show=False, matplotlib=True)
        else:
            shap_values = self.explainer.shap_values(X)
        
        return shap_values
                


        
    


    