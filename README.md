# python-package

Creating a Python package written in C.

### **Structure the project**

Create a clean folder structure that:
- separates Python code from C code
- places all code within `src/` to keep it separate from top-level metadata and documentation

```
project-name/
├── src/
│   ├── c/
│   │   ├── model_core.c
│   │   ├── model_core.h
│   │   └── model_core.dll  <- compiled DLL (from .c)
│   └── python/
│       ├── setup.py
│       └── model_client/
│           ├── __init__.py
│           └── wrapper.py  <- Python bindings via ctypes
```

### **Write the C library**

Write C code. For example:

```c
// model_core.c

#include <stdio.h>

int simple_function(int a, int b)
{
    return a + b;
}
```

Include function prototypes in a corresponding `.h` file:

```c
// model_core.h

#ifndef MODEL_CORE_H
#define MODEL_CORE_H

int simple_function(int a, int b);

#endif
```

### **Compile the C code into a DLL**

Use an appropriate toolchain (e.g. MSYS2 with `gcc`):

```bash
gcc -shared -o model_core.dll model_core.c
```

This creates a DLL callable from Python via `ctypes`.

> The DLL architecture (32-bit vs 64-bit) must match the architecture of the Python interpreter.


### **Create Python bindings with `ctypes`**

In `wrapper.py`:

```python
import os
import ctypes

# Define path from `wrapper.py` location to `model_core.dll` location
here = os.path.abspath(os.path.dirname(__file__))
dll_path = os.path.join(here, "..", "..", "c", "model_core.dll")
model_core = ctypes.CDLL(os.path.abspath(dll_path))

# Define argument and return types
model_core.simple_function.argtypes = [ctypes.c_int, ctypes.c_int]
model_core.simple_function.restype = ctypes.c_int
```

`wrapper.py` does two things:
- defines a path from itself to the required `.dll`
- defines data types for arguments and return value


### **Write a `setup.py` file to install the package**

Inside `src/python/setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="model_client",
    version="0.1",
    packages=find_packages(),
)
```

This lets you install locally via:

```bash
pip install -e .
```


### **Test with a simple script**

In `main.py`:

```python
from model_client.wrapper import model_core

print(model_core.simple_function(3, 4))
```

