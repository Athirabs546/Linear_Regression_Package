from setuptools import setup, find_packages

setup(
    name="linear_regression_package",
    version="0.1.0",
    author="AuthorA",
    author_email="authora@yahoo.com",
    description="A Python package for Linear Regression with logging and utilities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Athirabs546/Linear_Regression_Package.git",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
    ]
)
