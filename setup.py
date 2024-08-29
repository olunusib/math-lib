from setuptools import setup, find_packages

setup(
    name="test-ci-python",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["unittest"],
    entry_points={
        "console_scripts": [
            "main=src.main:main",
        ],
    },
)
