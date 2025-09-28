from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from anime_sama_api import AnimeSama

from src.controller import download, episodes, downloads
from .controller import index
from .controller import search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.router)
app.include_router(search.router)
app.include_router(episodes.router)
app.include_router(download.router)
app.include_router(downloads.router)
