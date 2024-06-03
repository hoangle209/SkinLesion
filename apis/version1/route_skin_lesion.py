import filetype
from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse

from skinlesion import YOLO as skYOLO

import cv2
import json
import numpy as np
from typing import IO


def validate_file_size_type(file: IO):
    FILE_SIZE = 5097152 # 5MB

    accepted_file_types = ["image/png", "image/jpeg", "image/jpg", "image/heic", "image/heif", "image/heics", "png",
                          "jpeg", "jpg", "heic", "heif", "heics" 
                          ] 
    file_info = filetype.guess(file.file)
    if file_info is None:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Unable to determine file type",
        )

    detected_content_type = file_info.extension.lower()

    if (
        file.content_type not in accepted_file_types
        or detected_content_type not in accepted_file_types
    ):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Unsupported file type",
        )

    real_file_size = 0
    for chunk in file.file:
        real_file_size += len(chunk)
        if real_file_size > FILE_SIZE:
            raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Too large")


router = APIRouter()

model = skYOLO("./weights/best_skin_lesion_ep67.pt")
classes = model.names
with open('conf_thresh.json') as file:
    conf_thresh = json.load(file)


@router.post("/")
def create_user(image: UploadFile):
    if not image:
        return {"message": "No upload file sent"}

    validate_file_size_type(image)
    
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
