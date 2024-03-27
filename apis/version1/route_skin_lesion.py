from fastapi import APIRouter
from fastapi import UploadFile
from fastapi.responses import JSONResponse

from skinlesion import YOLO as skYOLO

import cv2
import numpy as np
import json

router = APIRouter()

model = skYOLO("./weights/best_skin_lesion_ep67.pt")
classes = model.names
with open('conf_thresh.json') as file:
    conf_thresh = json.load(file)


@router.post("/")
def create_user(image: UploadFile):
    if not image:
        return {"message": "No upload file sent"}

    img = cv2.imdecode(np.asarray(
            bytearray(image.file.read()),
            dtype="uint8"), cv2.IMREAD_COLOR)

    result = model(img, verbose=False)
    probs = result[0].probs

    top1_classes = int(probs.top1)
    top1conf_classes = float(probs.top1conf)
    top5_classes = probs.top5
    top5conf_classes = probs.top5conf

    label_to_probabilities = {}
    for idx, probability in zip(top5_classes, top5conf_classes):
        label_to_probabilities[classes[idx]] = float(probability)

    return JSONResponse(content={
        "predict": top1conf_classes >= conf_thresh.get(str(top1_classes)),
        "label_to_probabilities": label_to_probabilities
    })
