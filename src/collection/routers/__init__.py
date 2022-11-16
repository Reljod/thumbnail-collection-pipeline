from fastapi import APIRouter, UploadFile

router = APIRouter(prefix='/collection')

@router.post("/upload/", tags=["upload"])
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}