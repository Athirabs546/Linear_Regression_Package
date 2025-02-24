import numpy as np
import pandas as pd

def generate_synthetic_data(n_samples=100):
    """Generate synthetic linear data for testing."""
    X = np.random.rand(n_samples, 1) * 10  # Features
    y = 2.5 * X.squeeze() + np.random.randn(n_samples) * 2  # Labels
    return X, y
