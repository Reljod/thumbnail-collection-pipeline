from fastapi import UploadFile
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from PIL import Image
from typing import Optional
import os
import uuid

class Extension(Enum):
    JPEG = 'jpg'
    PNG = 'png'


@dataclass
class Metadata:
    filename: str
    raw_filename: str
    metadata_filename: str
    date_uploaded_iso: Optional[str] = ''
    size: Optional[int] = 0
    height: Optional[int] = 0
    width: Optional[int] = 0

class MetadataBuilder:
    
    def __init__(self, file: UploadFile, ext: Extension = Extension.JPEG) -> None:
        self.file: UploadFile = file
        self.raw_filename = file.filename
        self.basename = self._generateUuidHex()
        self.filename = self.createFilename(ext=ext)
        self.metadata_filename = self.createMetadataFilename()
    
    def createFilename(self, ext: Extension = Extension.JPEG):
        return f"{self.basename}.{ext.value}"
    
    def createMetadataFilename(self):
        return f"{self.basename}.json"
    
    def build(self, image_path: str) -> Metadata:
        
        image = Image.open(image_path)
        
        return Metadata(
            filename=self.filename,
            raw_filename=self.raw_filename,
            metadata_filename=self.metadata_filename,
            date_uploaded_iso=datetime.isoformat(datetime.now()),
            size=os.path.getsize(image_path),
            height=image.height,
            width=image.width
        )
    
    def _generateUuidHex(self):
        return uuid.uuid4().hex