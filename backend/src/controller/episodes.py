import json
from anime_sama_api import AnimeSama
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

import config


router = APIRouter()


@router.get("/episodes/")
async def episodes(name: str | None = None, season_name: str | None = None):
    if name is None or season_name is None:
        return {"error": "error"}
    anime_sama = AnimeSama(config.url)
    catalogues = await anime_sama.search(name)
    catalogue = catalogues[0]
    seasons = await catalogue.seasons()
    season = None
    for season in seasons:
        if season.name == season_name:
            episodes = await season.episodes()
            return jsonable_encoder(episodes)
    return {"response": "ok"}
