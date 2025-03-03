from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        "cozyclib",
        ["cozyclib.pyx"],
        include_dirs=[],
        extra_compile_args=["-03"],
    )
]

setup(
    name="CozyOS SetupTools",
    ext_modules=cythonize(extensions),
    zip_safe=False,
)
