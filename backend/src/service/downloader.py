from typing import Any
from anime_sama_api import Episode, Lang
import yt_dlp

from config import download_path
from src.model.task import DownloadQueue, DownloadTask

download_tasks: list[DownloadQueue] = []
download_queue: list[DownloadQueue] = []


def download(episode: Episode, lang: Lang):
    task = DownloadQueue(episode, lang)
    if len(download_tasks) == 0:
        add_download_task(task)
    else:
        download_queue.append(task)


def add_download_task(task: DownloadQueue):
    player = task.episode.languages.availables[task.language][0][0]
    full_path = f"{download_path}/{task.episode.serie_name} - {task.episode.season_name} - {task.episode.name}"

    def download_hook(data: dict[str, Any]):
        status = data["status"]
        match status:
            case "downloading":
                if task.download is None:
                    task.download = DownloadTask()
                task.download.total_bytes = data.get("total_bytes") or data.get(
                    "total_bytes_estimate"
                )
                task.download.downloaded_bytes = data.get("downloaded_bytes", 0)
            case "finished":
                if task in download_tasks:
                    download_tasks.remove(task)
                    next_task = download_queue.pop(0)
                    add_download_task(next_task)

    opts = {
        "progress_hooks": [download_hook],
        "outtmpl": f"{full_path}.%(ext)s",
    }
    with yt_dlp.YoutubeDL(opts) as ytd:
        ytd.download(player)
