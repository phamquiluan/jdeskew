from os import path

import cv2
import numpy as np

from jdeskew.estimator import get_angle
from jdeskew.utility import rotate


def test_basic():
    image = np.zeros((512, 512), dtype=np.uint8)
    assert get_angle(image) == 0.0


def test_text_image_multiple_angle():
    image = cv2.imread(path.join(path.dirname(__file__), "test.png"))
    for angle in range(-10, 10):
        skew_image = rotate(image, angle=angle, resize=False)
        estimated_angle = get_angle(skew_image, vertical_image_shape=512)
        assert abs(angle + estimated_angle) < 0.5, f"{angle} - {estimated_angle}"
