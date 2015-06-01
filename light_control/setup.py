from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'Light Control API',
  ext_modules = cythonize("lights.pyx"),
)

