# Document Image Skew Estimation

[![pypi package](https://img.shields.io/pypi/v/jdeskew.svg)](https://pypi.org/project/jdeskew)
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/phamquiluan/jdeskew/tree/master.svg?style=svg&circle-token=f409daaab0e6671c81bb4b266b387fe933c131eb)](https://dl.circleci.com/status-badge/redirect/gh/phamquiluan/jdeskew/tree/master)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/25553a5195074e37a01dd3370c55abaa)](https://www.codacy.com/gh/phamquiluan/jdeskew/dashboard?utm_source=github.com&utm_medium=referral&utm_content=phamquiluan/jdeskew&utm_campaign=Badge_Coverage)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/25553a5195074e37a01dd3370c55abaa)](https://www.codacy.com/gh/phamquiluan/jdeskew/dashboard?utm_source=github.com&utm_medium=referral&utm_content=phamquiluan/jdeskew&utm_campaign=Badge_Grade)
[![Downloads](https://static.pepy.tech/personalized-badge/jdeskew?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/jdeskew)
![example workflow](https://github.com/phamquiluan/jdeskew/actions/workflows/dependency-review.yml/badge.svg)
![example workflow](https://github.com/phamquiluan/jdeskew/actions/workflows/python-package.yml/badge.svg)
![example workflow](https://github.com/phamquiluan/jdeskew/actions/workflows/docker-build-and-push.yml/badge.svg)
![example workflow](https://github.com/phamquiluan/jdeskew/actions/workflows/python-publish.yml/badge.svg)
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/adaptive-radial-projection-on-fourier/document-image-skew-estimation-on-dise-2021)](https://paperswithcode.com/sota/document-image-skew-estimation-on-dise-2021?p=adaptive-radial-projection-on-fourier)


![Cover Image](https://user-images.githubusercontent.com/24642166/165683091-4091bb3c-6625-4180-93b6-86deec9a0750.gif)

**Table of Contents**

- [Document Image Skew Estimation](#document-image-skew-estimation)
  - [Installation](#installation)
    - [pip](#pip)
  - [How-to-use](#how-to-use)
    - [using python](#using-python)
    - [Docker](#docker)
    - [using cog](#using-cog)
  - [Download Paper](#download-paper)
  - [Performance Comparison on DISE 2021](#performance-comparison-on-dise-2021)
  - [DISE 2021 Dataset](#dise-2021-dataset)
  - [Reproducibility and Evaluation Code](#reproducibility-and-evaluation-code)
  - [Citation](#citation)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Installation

### pip

```bash
pip install jdeskew
```

## How-to-use

### using python

```python
from jdeskew.estimator import get_angle
angle = get_angle(image)

from jdeskew.utility import rotate
output_image = rotate(image, angle)
```

### Docker

https://hub.docker.com/r/phamquiluan/jdeskew/tags


```bash
# build 
DOCKER_BUILDKIT=1 docker build -t jdeskew .

# run
docker run -p 8000:80 jdeskew

# test
curl -v -F file=@sample.png localhost:8000/predict
```


### using cog

https://github.com/replicate/cog

```bash
cog build --debug
cog predict -i input=@skew.png

# Output:
# Running prediction...
# {
#   "angle": -0.12520868113522532
# }
```

## Download Paper

Link1: https://ieeexplore.ieee.org/document/9897910

Link2: https://www.researchgate.net/publication/364320913_ADAPTIVE_RADIAL_PROJECTION_ON_FOURIER_MAGNITUDE_SPECTRUM_FOR_DOCUMENT_IMAGE_SKEW_ESTIMATION


## Performance Comparison on DISE 2021

CE: Correct Estimation rate

WE: Worst Error

|                      |   AED    |  TOP80   |    CE    |    WE    |
| :------------------: | :------: | :------: | :------: | :------: |
|     FredsDeskew      |  10.82   |   0.09   |   0.54   |   109    |
|      PypiDeskew      |  16.59   |   0.24   |   0.2    |   141    |
| Koo, Hyung Il et al. |   0.22   |   0.09   |   0.48   |   9.43   |
|       CMC-MSU        |   0.27   |   0.11   |   0.43   |   23.2   |
|     LRDE-EPITA-a     |   0.14   |   0.06   |   0.66   |  10.61   |
|                      |          |          |          |          |
|      Our (1024)      |   0.11   |   0.07   |   0.67   | **1.13** |
|      Our (1500)      |   0.09   |   0.05   |   0.78   | **1.13** |
|      Our (2048)      |   0.08   | **0.04** |   0.84   | **1.13** |
|      Our (3072)      | **0.07** | **0.04** | **0.86** | **1.13** |
|      Our (4096)      |   0.08   | **0.04** |   0.83   |   1.18   |

## DISE 2021 Dataset

This datasets are built upon three other datasets: DISEC 2013, RVL-CDIP, RDCL 2017. So I urge you to respect their LICENSE.

| Dataset Name          | URL                                                                                |
| --------------------- | ---------------------------------------------------------------------------------- |
| DISE 2021 (45 degree) | https://drive.google.com/file/d/1a-a6aOqdsghjeHGLnCLsDs7NoJIus-Pw/view?usp=sharing |
| DISE 2021 (15 degree) | https://drive.google.com/file/d/1BLiuu-j28dbuPFi4n3C0KuV6vXGmB0qS/view?usp=sharing |

Can also download from Zenodo: https://zenodo.org/records/12570649

## Reproducibility and Evaluation Code

Check the [reproduce.ipynb](reproduce.ipynb) file

## Citation

L. Pham, H. Hoang, X.T. Mai, T. A. Tran, "Adaptive Radial Projection on Fourier Magnitude Spectrum for Document Image Skew Estimation", ICIP, 2022.

```latex
@inproceedings{pham2021dise,
  title={Adaptive Radial Projection on Fourier Magnitude Spectrum for Document Image Skew Estimation},
  author={Luan Pham, Hao Hoang, Toan Mai, and Tuan Anh Tran},
  booktitle={2022 29th International Conference on Image Processing (ICIP)},
  year={2022},
  organization={IEEE}
}
```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=phamquiluan/jdeskew&type=Date)](https://star-history.com/#phamquiluan/jdeskew&Date)
