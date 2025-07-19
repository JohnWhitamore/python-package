import numpy as np

from model_client.api import create_design_matrix

dm = create_design_matrix(5, 6)
print("Design matrix:", dm)

# print("Synthetic data output:", model_core.generate_synthetic_data(1.23))
# print("Regression result:", model_core.run_regression(2.0, 3.0))