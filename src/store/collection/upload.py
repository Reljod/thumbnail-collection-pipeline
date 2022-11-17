from dataclasses import dataclass
from enum import Enum
from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder
from typing import Optional
from .metadata import MetadataBuilder, Metadata, Extension
import aiofiles
import os
import asyncio
import json


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
        
    async def multiple_upload(self, files: list[UploadFile]) -> list[Metadata]:
        coros = [ self.upload(file) for file in files ]
        metadata_list = await asyncio.gather(*coros)
        if (metadata_list == None):
            return []
        
        return list(metadata_list)
    
    async def upload(self, file: UploadFile) -> Metadata | None:
        metadata_builder = MetadataBuilder(file)
        
        img_full_path = self._get_full_path(metadata_builder.filename)
        await self.upload_image(file, img_full_path)
        
        metadata = metadata_builder.build(img_full_path)
        await self.upload_metadata(self._get_full_path(metadata_builder.metadata_filename), metadata)
        
        return metadata
    
    async def upload_image(self, file: UploadFile, img_full_path: str) -> Result:
        async with aiofiles.open(img_full_path, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)
  
    
    async def upload_metadata(self, file_path: str, metadata: Metadata):
        metadata_json = jsonable_encoder(metadata)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(metadata_json, f, indent=4)
    
    def _get_full_path(self, filename):
        return os.path.join(self.base_path, filename)
    
