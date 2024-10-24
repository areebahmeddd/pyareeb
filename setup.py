from setuptools import setup, find_packages

setup(
    name='pyareeb',
    version='0.1',
    description='Python package for Areeb',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "areeb-status = pyareeb:status",
        ]
    }
)
