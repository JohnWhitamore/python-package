from setuptools import setup, find_packages
import os
import shutil

# Copy DLL into package if not present
here = os.path.abspath(os.path.dirname(__file__))
dll_src = os.path.join(here, "..", "c", "model_core.dll")
dll_dest = os.path.join("model_client", "model_core.dll")
if not os.path.exists(dll_dest):
    shutil.copy(dll_src, dll_dest)

setup(
    name="model_client",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={"model_client": ["model_core.dll"]},
    description="Python wrapper for model_core C functions",
)