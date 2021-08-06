from fastapi.param_functions import Depends
from src.schemas import EchoDto
import aiohttp
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, Response

import settings

from ..utils import ElapsedTime

params = {"status": settings.PROXY_STATUS, "body": settings.BODY}


router = APIRouter(tags=["aiohttp"])


@router.get(
    "/api/proxy/picsum/aiohttp",
    description="Proxy Pictures using aiohttp",
    name="Pictures aiohttp proxy",
)
async def proxy(request: Request):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://picsum.photos/3000") as r:

            headers = {
                k.decode("UTF-8"): v.decode("UTF-8")
                for k, v in r.raw_headers
                if k.decode("UTF-8").lower()
                in [
                    "content-disposition",
                    "transfer-encoding",
                    "content-type",
                    "accept-ranges",
                    "vary",
                ]
            }

            return Response(
                await r.read(), status_code=r.status, headers=headers
            )


@router.get(
    "/api/proxy/pdf/aiohttp",
    description="Proxy PDF using aiohttp",
    name="PDF aiohttp proxy",
)
async def pdf_aiohttp(request: Request):
    async with aiohttp.ClientSession() as session:
        async with session.get("http://www.orimi.com/pdf-test.pdf") as r:

            headers = {
                k.decode("UTF-8"): v.decode("UTF-8")
                for k, v in r.raw_headers
                if k.decode("UTF-8").lower()
                in [
                    "content-disposition",
                    "transfer-encoding",
                    "content-type",
                    "accept-ranges",
                    "vary",
                ]
            }

            return Response(
                await r.read(), status_code=r.status, headers=headers
            )


params = {"status": settings.PROXY_STATUS, "body": settings.BODY}


@router.get(
    "/api/proxy/html/aiohttp",
    description="Proxy text/html using aiohttp",
    name="HTML aiohttp proxy",
)
async def html_aiohttp(request: Request, body: EchoDto = Depends()):
    clock = ElapsedTime()
    clock.start()
    async with aiohttp.ClientSession() as session:
        params.update({
            "body": body.message
        })
        async with session.get(
            settings.PROXY_URL, allow_redirects=True, params=params
        ) as r:
            response = await r.text()
            clock.done()
            response += clock.result
            return HTMLResponse(response, status_code=r.status)


@router.get(
    "/api/proxy/json/aiohttp",
    description="Proxy JSON using aiohttp",
    name="JSON aiohttp proxy",
)
async def json_aiohttp(request: Request):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://jsonplaceholder.typicode.com/todos"
        ) as r:
            return JSONResponse(await r.json(), status_code=r.status)
