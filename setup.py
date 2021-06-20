from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="argparse_node",
    python_requires=">=3.6.0",
    version="0.0.1",
    description="A minimal multi-level argument parser for your Python cli apps.",
    author="enhuiz",
    author_email="niuzhe.nz@outlook.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["anytree"],
    url="https://github.com/enhuiz/argparse_node",
)
