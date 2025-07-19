# main.py

from model_client.wrapper import model_core

print("\n📐 Design matrix size:", model_core.create_design_matrix(5, 6))
print("🔧 Synthetic data output:", model_core.generate_synthetic_data(1.23))
print("📊 Regression result:", model_core.run_regression(2.0, 3.0))