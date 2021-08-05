import httpx
from fastapi import APIRouter
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, Response

import settings

from ..utils import ElapsedTime

router = APIRouter(tags=["httpx"])


@router.get(
    "/api/proxy/picsum/httpx",
    description="Proxy Pictures using httpx",
    name="Pictures httpx proxy",
)
async def proxy(request: Request):
    async with httpx.AsyncClient() as client:
        req = client.build_request("GET", "https://picsum.photos/3000")
        r = await client.send(req, stream=True)
        headers = {
            k: v
            for k, v in r.headers.items()
            if k
            in [
                "content-disposition",
                "transfer-encoding",
                "content-type",
                "accept-ranges",
                "vary",
            ]
        }

        return Response(
            await r.aread(), status_code=r.status_code, headers=headers
        )


@router.get(
    "/api/proxy/pdf/httpx",
    description="Proxy PDF using httpx",
    name="PDF httpx proxy",
)
async def pdf_httpx(request: Request):
    async with httpx.AsyncClient() as client:
        req = client.build_request("GET", "http://www.orimi.com/pdf-test.pdf")
        r = await client.send(req, stream=True)
        headers = {
            k: v
            for k, v in r.headers.items()
            if k
            in [
                "content-disposition",
                "transfer-encoding",
                "content-type",
                "accept-ranges",
                "vary",
            ]
        }

        return Response(
            await r.aread(), status_code=r.status_code, headers=headers
        )


params = {"status": settings.PROXY_STATUS, "body": settings.BODY}


@router.get(
    "/api/proxy/html/httpx",
    description="Proxy text/html using httpx",
    name="HTML httpx proxy",
)
async def html_httpx(request: Request):
    clock = ElapsedTime()
    clock.start()
    async with httpx.AsyncClient() as client:
        r = await client.request("GET", settings.PROXY_URL, params=params)
        clock.done()
        return HTMLResponse(r.text + clock.result)


params = {"status": settings.PROXY_STATUS, "body": settings.BODY}


@router.get(
    "/api/proxy/json/httpx",
    description="Proxy JSON using httpx",
    name="JSON httpx proxy",
)
async def json_httpx(request: Request):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "https://jsonplaceholder.typicode.com/todos", params=params
        )
        return JSONResponse(r.json(), status_code=r.status_code)
