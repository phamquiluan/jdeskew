"""Simple api."""
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/predict")
def predict(file: UploadFile):
    """simple predict function."""
    # read image
    import cv2
    import numpy as np

    content = file.file.read()
    nparr = np.fromstring(content, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # process image
    from jdeskew.estimator import get_angle

    angle = get_angle(image)

    return {"file_name": file.filename, "skew_angle": angle}
