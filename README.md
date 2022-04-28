# Document Image Skew Estimation

[![pypi package](https://img.shields.io/badge/version-v0.0.5-blue)](https://pypi.org/project/jdeskew)
[![CircleCI](https://circleci.com/gh/phamquiluan/jdeskew/tree/master.svg?style=shield&circle-token=37f6b4ef126f3e985db7c624d1d76f22a223cf41)](https://circleci.com/gh/phamquiluan/jdeskew/tree/master)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/25553a5195074e37a01dd3370c55abaa)](https://www.codacy.com/gh/phamquiluan/jdeskew/dashboard?utm_source=github.com&utm_medium=referral&utm_content=phamquiluan/jdeskew&utm_campaign=Badge_Coverage)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/25553a5195074e37a01dd3370c55abaa)](https://www.codacy.com/gh/phamquiluan/jdeskew/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=phamquiluan/jdeskew&amp;utm_campaign=Badge_Grade)

![Cover Image](https://user-images.githubusercontent.com/24642166/165683091-4091bb3c-6625-4180-93b6-86deec9a0750.gif)

## Installation

```bash
pip install -e .[dev]
```

## How-to-use

```python
from jdeskew.estimator import get_angle
angle = get_angle(image)

from jdeskew.utility import rotate
output_image = rotate(image, angle)
```

## Performance Comparison on DISE 2021

CE: Correct Estimation rate

WE: Worst Error

|                      |    AED   |   TOP80  |    CE    |    WE    |
|:--------------------:|:--------:|:--------:|:--------:|:--------:|
|      FredsDeskew     |   10.82  |   0.09   |   0.54   |    109   |
|      PypiDeskew      |   16.59  |   0.24   |    0.2   |    141   |
| Koo, Hyung Il et al. |   0.22   |   0.09   |   0.48   |   9.43   |
|        CMC-MSU       |   0.27   |   0.11   |   0.43   |   23.2   |
|     LRDE-EPITA-a     |   0.14   |   0.06   |   0.66   |   10.61  |
|                      |          |          |          |          |
|      Our (1024)      |   0.11   |   0.07   |   0.67   | **1.13** |
|      Our (1500)      |   0.09   |   0.05   |   0.78   | **1.13** |
|      Our (2048)      |   0.08   | **0.04** |   0.84   | **1.13** |
|      Our (3072)      | **0.07** | **0.04** | **0.86** | **1.13** |
|      Our (4096)      |   0.08   | **0.04** |   0.83   |   1.18   |

## Citation

L. Pham, T. A. Tran, "Document Image Skew Estimation using Adaptive
Radial Projection", 2022.

```latex
@misc{luandise2022,
  title={Document Image Skew Estimation using Adaptive Radial Projection},
  author={Luan, Pham and Tuan Anh, Tran},
  url={https://github.com/phamquiluan/jdeskew},
  year={2022}
}
```
