from fastapi import APIRouter, UploadFile

from ..lib import upload
from ...store.collection import Metadata


router = APIRouter(prefix='/collection')

@router.post("/upload/", tags=["upload"])
async def upload_multiple_files(files: list[UploadFile]) -> list[Metadata]:
    return await upload.upload_multiple_files(files)

