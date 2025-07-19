import ctypes
import os

here = os.path.abspath(os.path.dirname(__file__))
dll_path = os.path.join(here, "..", "..", "c", "model_core.dll")
model_core = ctypes.CDLL(os.path.abspath(dll_path))
model_core = ctypes.CDLL(dll_path)

# Declare function signatures
model_core.create_design_matrix.argtypes = [ctypes.c_int, ctypes.c_int]
model_core.create_design_matrix.restype = ctypes.POINTER(ctypes.c_int)

model_core.generate_synthetic_data.argtypes = [ctypes.c_double]
model_core.generate_synthetic_data.restype = ctypes.c_double

model_core.run_regression.argtypes = [ctypes.c_double, ctypes.c_double]
model_core.run_regression.restype = ctypes.c_double

# Call the functions
print("[Python] Design matrix size:", model_core.create_design_matrix(3, 4))
print("[Python] Synthetic output:", model_core.generate_synthetic_data(1.5))
print("[Python] Regression result:", model_core.run_regression(2.0, 3.0))