from anime_sama_api import AnimeSama, Lang, Languages, langs
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from src.service import downloader
from pydantic import BaseModel
import threading

import config


class Episode(BaseModel):
    serie_name: str
    season_index: int
    language: str
    episode_index: int


router = APIRouter()


@router.post("/download")
async def download(episode: Episode):
    print(episode)
    anime_sama = AnimeSama(config.url)
    catalogues = await anime_sama.search(episode.serie_name)
    catalogue = catalogues[0]
    seasons = await catalogue.seasons()
    season = None
    season = seasons[episode.season_index]
    episodes = await season.episodes()
    download_thread = threading.Thread(
        target=downloader.download,
        args=(episodes[episode.episode_index], episode.language),
    )
    download_thread.start()
    # for i in episodes_index:
    #     downloader.download(episodes[i], language)
    return {"response": "ok"}
