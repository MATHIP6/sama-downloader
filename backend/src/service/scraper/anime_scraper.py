import cloudscraper
from bs4 import BeautifulSoup

from .catalogue import Catalogue


class AnimeScraper:
    def __init__(self, url: str) -> None:
        self.url = url
        self.client = cloudscraper.create_scraper()

    def search(self, query: str) -> list[Catalogue]:
        res = self.client.post(
            f"{self.url}/template-php/defaut/fetch.php", data={"query": query}
        )
        # print(res.content)
        soup = BeautifulSoup(res.content, "html.parser")
        catalogues: list[Catalogue] = []
        # print(soup.findAll())
        for balise in soup.find_all("a"):
            url = balise.get("href")
            image = balise.img["src"]
            name = balise.div.h3.text
            alternative_names = balise.div.p.text.split(", ")
            catalogues.append(Catalogue(url, name, alternative_names, image))

        return catalogues
