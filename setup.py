import os
import pathlib
from setuptools import setup, find_packages

# python setup.py sdist bdist_wheel
# twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*

# get __version__ from _version.py
ver_file = os.path.join("pyworkforce", "_version.py")
with open(ver_file) as f:
    exec(f.read())

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="pyworkforce",
    version=__version__,
    description="Common tools for workforce management, schedule and optimization problems",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rodrigo-arenas/pyworkforce",
    author="Rodrigo Arenas",
    author_email="rodrigo.arenas456@gmail.com",
    license="MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(include=['pyworkforce', 'pyworkforce.*']),
    install_requires=[
        'numpy',
        'ortools>=7.8.7959',
        'pandas',
        'joblib>=0.11'
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
