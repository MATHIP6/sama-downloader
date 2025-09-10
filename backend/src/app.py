from fastapi import FastAPI
from anime_sama_api import AnimeSama

from src.controller import download, episodes, downloads
from .controller import index
from .controller import search

app = FastAPI()


app.include_router(index.router)
app.include_router(search.router)
app.include_router(episodes.router)
app.include_router(download.router)
app.include_router(downloads.router)
