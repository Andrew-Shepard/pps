from infrastructure.api.dependencies.errors import DependencyNotInitialized
from infrastructure.api.dependencies.session import CLIENT_SESSION, get_client_session
from infrastructure.client.http.common import PPSHTTPClient

PPS_HTTP_CLIENT = None

async def init_PPSHTTPClient():
    global PPS_HTTP_CLIENT
    if CLIENT_SESSION is None:
        await get_client_session()
    PPS_HTTP_CLIENT = PPSHTTPClient(None,None,CLIENT_SESSION)
    return PPS_HTTP_CLIENT

async def get_PPSHTTPClient():
    if PPS_HTTP_CLIENT is None:
        raise DependencyNotInitialized("PPSHTTPClient not initialized")
    return PPS_HTTP_CLIENT