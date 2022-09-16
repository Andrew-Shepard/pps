import urllib.parse
from typing import Mapping

from aiohttp import ClientSession


class http_client:
    def __init__(self, reporter, host: str, client_session: ClientSession) -> None:
        self.host = host
        self.reporter = reporter
        self.client_session = client_session
    
    @property
    def headers(self):
        return {"content-type": "application/json"}

    async def do_get(self, url: str):
        async with self.client_session.get(url, headers=self.headers) as resp:
            _resp = await resp.json()
            return _resp