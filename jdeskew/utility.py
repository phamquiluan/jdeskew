"""Utility."""
import cv2


def rotate(image, angle, resize=True, border_mode=None, border_value=None, flags=None):
    """
    Rotate input image with respect to a given angle.

    Parameters
    ----------
    image : np.ndarray
        Input image.
    angle : float
        Rotation angle in degrees.
    resize : bool
        Resize output to the input image shape.
    border_mode : int, optional
        cv2.BORDER_REPLICATE or cv2.BORDER_CONSTANT.
    border_value : optional
        Border value used when border_mode is cv2.BORDER_CONSTANT.
    flags : int, optional
        OpenCV interpolation flags.

    Returns
    -------
    np.ndarray
        Rotated image.

    """
    if border_mode is None:
        border_mode = cv2.BORDER_CONSTANT
    if flags is None:
        # flags=cv2.INTER_NEAREST
        flags = cv2.INTER_LINEAR

    h, w = image.shape[:2]
    M = cv2.getRotationMatrix2D(center=(w // 2, h // 2), angle=angle, scale=1.0)
    output_image = cv2.warpAffine(
        src=image,
        M=M,
        dsize=(w, h),
        flags=flags,
        borderMode=border_mode,
        borderValue=None if border_mode == cv2.BORDER_REPLICATE else border_value,
    )

    if resize is True:
        output_image = cv2.resize(output_image, (w, h))
    return output_image
