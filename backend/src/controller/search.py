from anime_sama_api import AnimeSama
from fastapi import APIRouter

import config

router = APIRouter()


@router.get("/search/{name}")
async def search(name: str):
    anime_sama = AnimeSama(config.url)
    catalogues = await anime_sama.search(name)
    response = []
    for catalogue in catalogues:
        response.append(
            {
                "name": catalogue.name,
                "image_url": catalogue.image_url,
                "genres": catalogue.genres,
                "seasons": [season.name for season in await catalogues[0].seasons()],
            }
        )
    return response
