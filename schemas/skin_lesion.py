from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile


class SkinImageUpload(BaseModel):
    image: Optional[UploadFile] = None
