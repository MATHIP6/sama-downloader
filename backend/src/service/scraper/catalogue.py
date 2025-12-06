from typing import Sequence

import cloudscraper

from season import Season


class Catalogue:
    def __init__(
        self,
        url: str,
        name: str,
        alternative_names: Sequence[str] | None = None,
        image_url: str = "",
        genres: list[str] = [],
        synopsis: str = "",
        client: cloudscraper.CloudScraper | None = None,
    ) -> None:
        if alternative_names is None:
            alternative_names = []

        self.url = url
        self.site_url = url.split("/")[0] + "/"
        self.client = client or cloudscraper.create_scraper()

        self.name = name

        self.alternative_names = alternative_names
        self.image_url = image_url

        self.genres = genres
        self.synopsis = synopsis

        self.seasons: list[Season] = []
