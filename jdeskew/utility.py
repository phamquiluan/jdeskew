"""Utility."""
import cv2


def rotate(image, angle, resize=True, border_mode=None, border_value=None):
    """Rotate input image respect to a given angle.

    Params:
    --------
    resize (Bool) : resize to input image shape
    border_mode : cv2.BORDER_REPLICATE, cv2.BORDER_CONSTANT
    border_value : when border_mode == cv2.BORDER_CONSTANT
    """
    if border_mode is None:
        border_mode = cv2.BORDER_CONSTANT

    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D(center=(w // 2, h // 2), angle=angle, scale=1.0)
    output_image = cv2.warpAffine(
        src=image,
        M=M,
        dsize=(w, h),
        # flags=cv2.INTER_CUBIC,
        flags=cv2.INTER_NEAREST,
        borderMode=border_mode,
        borderValue=None if border_mode == cv2.BORDER_REPLICATE else border_value,
    )

    if resize is True:
        output_image = cv2.resize(output_image, (w, h))
    return output_image
