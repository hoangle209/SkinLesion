from fastapi import APIRouter
from fastapi import Request
# from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import logging

logger = logging.getLogger(__name__)

templates = Jinja2Templates(directory="templates")
general_pages_router = APIRouter()


@general_pages_router.get("/")
async def home(request: Request):
    logger.info(f"Debug: {await request.body()}")
    return templates.TemplateResponse("pages/index.html", {
        "request": request
    })
