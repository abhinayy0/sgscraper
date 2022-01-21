from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint

class ScrapeView(HTTPEndpoint):

    async def get(self, request):
        return JSONResponse({"message":"hello"})