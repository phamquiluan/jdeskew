import numpy as np


def test_basic():
    from jdeskew import get_angle

    image = np.zeros((512, 512), dtype=np.uint8)

    assert get_angle(image) == 0.
