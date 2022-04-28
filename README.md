# Document Image Skew Estimation

[![CircleCI](https://circleci.com/gh/phamquiluan/jdeskew/tree/master.svg?style=svg&circle-token=37f6b4ef126f3e985db7c624d1d76f22a223cf41)](https://circleci.com/gh/phamquiluan/jdeskew/tree/master)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/25553a5195074e37a01dd3370c55abaa)](https://www.codacy.com/gh/phamquiluan/jdeskew/dashboard?utm_source=github.com&utm_medium=referral&utm_content=phamquiluan/jdeskew&utm_campaign=Badge_Coverage)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/25553a5195074e37a01dd3370c55abaa)](https://www.codacy.com/gh/phamquiluan/jdeskew/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=phamquiluan/jdeskew&amp;utm_campaign=Badge_Grade)

![](https://user-images.githubusercontent.com/24642166/165683091-4091bb3c-6625-4180-93b6-86deec9a0750.gif)

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
