class Season:
    def __init__(self, name: str, url: str):
        self.name = name
        self.url = url
        self.seasons: list[Season] = []

    def episodes(self):
        pass
