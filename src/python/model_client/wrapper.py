import ctypes
import os

# File paths
here = os.path.abspath(os.path.dirname(__file__))
dll_path = os.path.join(here, "..", "..", "c", "model_core.dll")

# DLL types
model_core = ctypes.CDLL(os.path.abspath(dll_path))

# Types for function signatures
model_core.create_design_matrix.argtypes = [ctypes.c_int, ctypes.c_int]
model_core.create_design_matrix.restype = ctypes.POINTER(ctypes.c_double)

model_core.generate_synthetic_data.argtypes = [ctypes.c_double]
model_core.generate_synthetic_data.restype = ctypes.c_double

model_core.run_regression.argtypes = [ctypes.c_double, ctypes.c_double]
model_core.run_regression.restype = ctypes.c_double