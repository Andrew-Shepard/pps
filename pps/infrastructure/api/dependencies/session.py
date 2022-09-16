from typing import Optional

from aiohttp import ClientSession

CLIENT_SESSION: Optional[ClientSession] = None

async def get_client_session():
    global CLIENT_SESSION
    if CLIENT_SESSION is None:
        CLIENT_SESSION = ClientSession()
    return CLIENT_SESSION