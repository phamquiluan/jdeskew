"""Tests."""
from os import path

import cv2
import numpy as np
import pytest

from jdeskew.estimator import get_angle
from jdeskew.utility import rotate


def test_basic():
    """Test basic."""
    image = np.zeros((512, 512), dtype=np.uint8)
    assert get_angle(image) == 0.0


@pytest.mark.parametrize("angle", list(range(-10, 10)))
def test_text_image_angle_range_10(angle: int):
    """Test_text_image_angle_range_10."""
    image = cv2.imread(path.join(path.dirname(__file__), "test.png"))
    skew_image = rotate(image, angle=angle, resize=False)
    estimated_angle = get_angle(skew_image, vertical_image_shape=512)
    assert abs(angle + estimated_angle) < 0.5, f"{angle} - {estimated_angle}"


@pytest.mark.parametrize("angle", list(range(-44, 44)))
def test_text_image_angle_range_44(angle: int):
    """Test_text_image_angle_range_44."""
    image = cv2.imread(path.join(path.dirname(__file__), "test.png"))
    skew_image = rotate(image, angle=angle, resize=False)
    estimated_angle = get_angle(skew_image, vertical_image_shape=512, angle_max=44.9)
    assert abs(angle + estimated_angle) < 0.5, f"{angle} - {estimated_angle}"
