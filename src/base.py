from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import RedirectResponse

router = APIRouter(tags=["Base"])


@router.get(
    "/api/base", description="Basic routing for testing", name="Basic Routing"
)
async def proxy(request: Request):
    return {"demo": "demo"}


@router.get("/", include_in_schema=False)
async def api_doc(request: Request):
    return RedirectResponse("/docs")
