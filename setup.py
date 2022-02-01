from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="argparse_node",
    python_requires=">=3.7.0",
    version="0.0.3",
    description="A minimal multi-level argument parser for your Python cli apps.",
    author="enhuiz",
    author_email="niuzhe.nz@outlook.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["argparse_node"],
    install_requires=["anytree"],
    url="https://github.com/enhuiz/argparse_node",
)
