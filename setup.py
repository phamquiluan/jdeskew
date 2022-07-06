"""Setup file for jdeskew package."""
import os

from setuptools import find_packages, setup

version = None
with open("README.md") as ref:
    data = ref.readlines()[2]
    version = data[data.find("version-v") + 9 : data.find("-blue")]
    assert version is not None, data

cwd = os.path.dirname(os.path.abspath(__file__))


def __write_version_file():
    version_path = os.path.join(cwd, "jdeskew", "version.py")
    with open(version_path, "w") as f:
        f.write(f"__version__ = '{version}'\n")


__write_version_file()

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
    extras_require={
        "dev": [
            "black",
            "pytest",
            "coverage",
            "pre-commit",
            "pytest-xdist",
            "fastapi",
            "uvicorn[standard]",
            "python-multipart",
        ]
    },
)
