from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.responses import JSONResponse

from scraper.views import ScrapeView
   

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = JSONResponse({'hello': 'world'})
    await response(scope, receive, send)

routes = [
    Route('/scrape',ScrapeView ),
    Mount('/static', StaticFiles(directory="static")),
]

app = Starlette(debug=True, routes=routes)