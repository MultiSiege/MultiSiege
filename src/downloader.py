import steam.monkey
steam.monkey.patch_minimal()

from steam.client.cdn import *
from steam.client import SteamClient

class Downloader:
    def __init__(self) -> None:
        """
        Spawns a new downloader instance, which comes bundled with the UI.
        """