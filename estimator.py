"""Estimator for cog users."""
from typing import Dict

import numpy as np
from cog import BasePredictor, Input, Path
from PIL import Image

from jdeskew.estimator import get_angle


class Estimator(BasePredictor):
    """Cog estimator."""

    def predict(self, input_path: Path = Input()) -> Dict:
        """Run a single prediction on the model."""
        im = np.array(Image.open(str(input_path)))
        angle = get_angle(im)
        return {"angle": angle}
