"""Skew Estimator."""
import cv2
import numpy as np
from typing import Optional


def _ensure_gray(image: np.ndarray) -> np.ndarray:
    try:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except cv2.error:
        pass
    return image


def _ensure_optimal_square(image: np.ndarray) -> np.ndarray:
    assert image is not None, image
    nw = nh = cv2.getOptimalDFTSize(max(image.shape[:2]))
    output_image = cv2.copyMakeBorder(
        src=image,
        top=0,
        bottom=nh - image.shape[0],
        left=0,
        right=nw - image.shape[1],
        borderType=cv2.BORDER_CONSTANT,
        value=255,
    )
    return output_image


def _get_fft_magnitude(image: np.ndarray) -> np.ndarray:
    gray = _ensure_gray(image)
    opt_gray = _ensure_optimal_square(gray)

    # thresh
    opt_gray = cv2.adaptiveThreshold(
        ~opt_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, -10
    )

    # perform fft - using fft2 to ensure square output
    dft = np.fft.fft2(opt_gray)
    shifted_dft = np.fft.fftshift(dft)

    # get the magnitude (module)
    magnitude = np.abs(shifted_dft)
    return magnitude


def _get_angle_radial_projection(m: np.ndarray, angle_max: Optional[float] = None, num: Optional[int] = None) -> float:
    """Get angle via radial projection.

    Arguments:
    ------------
    angle_max : float
    num : int
      number of angles to generate between 1 degree
    """
    assert m.shape[0] == m.shape[1]
    r = c = m.shape[0] // 2

    if angle_max is None:
        angle_max = 15.0

    if num is None:
        num = 20

    tr = np.linspace(-1 * angle_max, angle_max, int(angle_max * num * 2)) / 180 * np.pi

    # Pre-allocate array for better performance
    li = np.zeros_like(tr)

    for i, t in enumerate(tr):
        x = np.arange(0, r)
        y = c + np.int32(x * np.cos(t))
        x = c + np.int32(-1 * x * np.sin(t))
        # Use boolean indexing for faster computation
        valid_indices = (y >= 0) & (y < m.shape[0]) & (x >= 0) & (x < m.shape[1])
        li[i] = np.sum(m[y[valid_indices], x[valid_indices]])

    a = tr[np.argmax(li)] / np.pi * 180

    if a == -1 * angle_max:
        return 0.0
    return float(a)


def get_angle(
    image: np.ndarray,
    vertical_image_shape: Optional[int] = None,
    angle_max: Optional[float] = None
) -> float:
    """Getting angle from a given document image.

    Args:
        image: Input image as numpy array
        vertical_image_shape: Optional resize height for preprocessing
        angle_max: Maximum angle to search for

    Returns:
        float: Estimated skew angle in degrees
    """
    assert isinstance(image, np.ndarray), image

    # if vertical_image_shape is None:
    #     vertical_image_shape = 512

    if angle_max is None:
        angle_max = 15.0

    # resize
    if vertical_image_shape is not None:
        ratio = vertical_image_shape / image.shape[0]
        image = cv2.resize(image, None, fx=ratio, fy=ratio)

    m = _get_fft_magnitude(image)
    a = _get_angle_radial_projection(m, angle_max=angle_max)
    return a
