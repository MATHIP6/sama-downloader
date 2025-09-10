from fastapi import APIRouter

from src.service import downloader


router = APIRouter()


@router.get("/downloads")
def downloads():
    return downloader.download_tasks + downloader.download_queue
