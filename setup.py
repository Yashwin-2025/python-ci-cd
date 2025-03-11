from setuptools import setup, find_packages
setup(
    name="python-ci-cd",  # Rename package here
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="A simple Python package for CI/CD testing.",
    author="Your Name",
)
