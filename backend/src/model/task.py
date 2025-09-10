from anime_sama_api import Episode, Lang


class DownloadQueue:
    def __init__(self, episode: Episode, language: Lang) -> None:
        self.is_downloading: bool = False
        self.episode: Episode = episode
        self.language: Lang = language
        self.download: DownloadTask | None = None


class DownloadTask:
    def __init__(self) -> None:
        self.download_speed: float = 0
        self.total_bytes: int = 0
        self.downloaded_bytes: int = 0
        pass
