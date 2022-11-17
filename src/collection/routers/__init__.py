from fastapi import APIRouter, UploadFile

from ...store.collection.metadata import Metadata
from ...store.collection import Uploader

router = APIRouter(prefix='/collection')
uploader = Uploader()

@router.post("/upload/", tags=["upload"])
async def create_upload_files(files: list[UploadFile]) -> list[Metadata]:
    metadata_list = await uploader.multiple_upload(files)
    return metadata_list