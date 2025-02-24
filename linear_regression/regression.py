import numpy as np
from sklearn.linear_model import LinearRegression
from .log_config import logger  # Import logger

class SimpleLinearRegression:
    def __init__(self):
        self.model = LinearRegression()
    
    def train(self, X, y):
        logger.info(f"Training started with {len(X)} samples.")
        self.model.fit(X, y)
        logger.info("Training completed successfully.")

    def predict(self, X):
        logger.info(f"Making predictions for {len(X)} samples.")
        return self.model.predict(X)
    
    def get_coefficients(self):
        return self.model.coef_, self.model.intercept_
