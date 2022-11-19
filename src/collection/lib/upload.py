
from fastapi import UploadFile
import asyncio
import os

from ...store.collection import Uploader, Metadata, MetadataBuilder

uploader = Uploader()

async def upload_file(file: UploadFile) -> Metadata:
    metadata_builder = MetadataBuilder(file)
    filename = metadata_builder.filename
    
    img_full_path: str = os.path.join(uploader.base_path, filename)
    await uploader.upload_image(file, filename)
    
    metadata = metadata_builder.build(img_full_path)
    await uploader.upload_metadata(metadata, metadata_builder.metadata_filename)
    
    return metadata

async def upload_multiple_files(files: list[UploadFile]) -> list[Metadata]:
    coros = [ upload_file(file) for file in files ]
    metadata_list = await asyncio.gather(*coros)
    if (metadata_list == None):
        return []

    return list(metadata_list)
        