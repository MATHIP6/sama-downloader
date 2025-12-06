import re
import cloudscraper
from bs4 import BeautifulSoup

from catalogue import Catalogue
from season import Season


class AnimeScraper:
    def __init__(self, url: str) -> None:
        self.url = url
        self.client = cloudscraper.create_scraper()

    def search(self, query: str) -> list[Catalogue]:
        res = self.client.post(
            f"{self.url}/template-php/defaut/fetch.php", data={"query": query}
        )
        soup = BeautifulSoup(res.content, "html.parser")
        catalogues: list[Catalogue] = []
        for balise in soup.find_all("a"):
            url = balise.get("href")
            image = balise.img["src"]
            name = balise.div.h3.text
            alternative_names = balise.div.p.text.split(", ")
            catalogues.append(Catalogue(url, name, alternative_names, image))

        return catalogues

    def get_anime(self, name: str) -> Catalogue:
        url = f"{self.url}/catalogue/{name}/"
        res = self.client.get(url)

        if res.status_code != 200:
            raise ValueError("Error status code: ", res.status_code)

        soup = BeautifulSoup(res.content, "html.parser")
        display_name = soup.find("h4", id="titreOeuvre").text
        alternative_names = soup.find("h2", id="titreAlter").text.split(", ")
        image_url: str = soup.find("img", id="coverOeuvre").get("src")
        synopsis = soup.find("p", class_="text-sm text-gray-300 leading-relaxed").text
        genres = soup.find("a", class_="text-sm text-gray-300").text.split(", ")

        seasons: list[Season] = []

        seasons_section = soup.find(
            "div",
            class_="flex flex-wrap overflow-y-hidden text-sm justify-start bg-slate-900 bg-opacity-70 rounded mt-2 h-auto",
        )

        pattern = r'panneauAnime\("(.+?)", *"(.+?)(?:vostfr|vf)"\);'

        matches = re.findall(pattern, str(seasons_section.contents))

        for name, path in matches:
            season = Season(name, f"{url}{path}")
            seasons.append(season)

        anime = Catalogue(url, name, alternative_names, image_url, genres, synopsis)
        anime.seasons = seasons

        return anime
