from fastapi import APIRouter, Depends, status
from fastapi.background import BackgroundTasks
from fastapi.responses import FileResponse

from files.schemas import FileDownload, FileUpload
from files.services import download_file, upload_file
from files.utils import remove_file

router = APIRouter(prefix="/files", tags=["files"])
import logging

logger = logging.getLogger()

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    tags=["files"],
)
async def file_upload(file: FileUpload = Depends()):
    logger.info("uploooooad")
    if uploaded := await upload_file(
        user_id=file.user_id, bucket_name=file.bucket_name, file=file.file
    ):
        return uploaded

