import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="secuuth-python-sdk",
    version="1.0.0",
    description="It verify and decode token",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/akum304/secuuth-jwt-python.git",
    author="Udit Vashisht",
    author_email="admin@saralgyaan.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["python-sdk"],
    include_package_data=True,
    install_requires=['json','jwt','requests'],
    
)