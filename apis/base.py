from fastapi import APIRouter

from apis.version1 import route_general_pages
from apis.version1 import route_skin_lesion


api_router = APIRouter()
api_router.include_router(
    route_general_pages.general_pages_router,
    prefix="",
    tags=["general_pages"]
)
api_router.include_router(
    route_skin_lesion.router,
    prefix="/api/v1/skin_lesion",
    tags=["skin_lesion"]
)
