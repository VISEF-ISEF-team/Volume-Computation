from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("_bitree_marching_cubes_cy.pyx"),
    include_dirs=[np.get_include()]
)