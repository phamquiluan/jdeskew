"""Setup file for jdeskew package."""
from setuptools import find_packages, setup

setup(
    name="jdeskew",
    description="Document Image Skew Estimation using Adaptive Radial Projection",
    author="Luan Pham",
    version="0.0.1",
    author_email="phamquiluan@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy", "opencv-python"],
    extras_require={"dev": ["black", "pytest", "coverage", "pre-commit"]},
)
