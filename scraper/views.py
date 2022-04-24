from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.templating import Jinja2Templates
from scraper.service import ScrapeData

templates = Jinja2Templates(directory='templates')

class ScrapeView(HTTPEndpoint):

    async def get(self, request):
        return templates.TemplateResponse('index.html', {'request': request})

    async def post(self, request):
        data =await request.form()
        scraping = ScrapeData(data["keyword"])
        scraping.start_scraping()

        return templates.TemplateResponse('searching.html', {'request': request})