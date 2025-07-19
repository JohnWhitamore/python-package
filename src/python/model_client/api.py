import numpy as np
import ctypes
from .wrapper import model_core
  
def create_design_matrix(rows, cols):
    
    # Call C function to allocate memory and create design matrix contents
    
    # ... design_matrix_raw is a pointer to the C array
    design_matrix_raw = model_core.create_design_matrix(rows, cols)
    
    # ... dimensions
    total_size = rows * cols;
    
    # Wrap pointer in NumPy view and reshape
    flat_array = np.ctypeslib.as_array(design_matrix_raw, shape=(total_size,))
    design_matrix_np = np.array(flat_array).reshape((rows, cols))
    
    # Displose of the C pointer cleanly
    
    # ... prepare a pointer-to-pointer (int**) for dispose_array
    ptr_type = model_core.create_design_matrix.restype
    ptr_ref = ctypes.pointer(design_matrix_raw)

    # ... bind the dispose_array signature
    model_core.dispose_array.argtypes = [ctypes.POINTER(ptr_type)]
    model_core.dispose_array.restype = None

    # ... call C function to free and nullify the pointer
    model_core.dispose_array(ptr_ref)
    
    return design_matrix_np

    

    

    
    

   