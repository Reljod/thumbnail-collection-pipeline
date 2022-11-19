from dataclasses import dataclass
from enum import Enum
from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder
from typing import Optional
import aiofiles
import os
import json

from .metadata import Metadata, Extension


@dataclass
class UploaderOptions:
    base_path: Optional[str] = './db/collection/raw_files'
    extension: Optional[Extension] = Extension.JPEG

options = UploaderOptions()

class Result(Enum):
    FAIL = 0
    OK = 1

class Uploader:
    
    def __init__(self, options: UploaderOptions = options):
        self.base_path = options.base_path
    
    async def upload_image(self, file: UploadFile, filename: str) -> Result:
        img_full_path = self._get_full_path(filename)
        async with aiofiles.open(img_full_path, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)
  
    
    async def upload_metadata(self, metadata: Metadata, filename: str):
        metadata_json = jsonable_encoder(metadata)
        file_path = self._get_full_path(filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(metadata_json, f, indent=4)
    
    def _get_full_path(self, filename):
        return os.path.join(self.base_path, filename)
    
