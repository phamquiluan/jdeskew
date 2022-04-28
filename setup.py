"""Setup file for jdeskew package."""
from setuptools import find_packages, setup

version = "0.0.2"

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="jdeskew",
    description="Document Image Skew Estimation using Adaptive Radial Projection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Luan Pham",
    version=version,
    author_email="phamquiluan@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy", "opencv-python"],
    extras_require={"dev": ["black", "pytest", "coverage", "pre-commit"]},
)
