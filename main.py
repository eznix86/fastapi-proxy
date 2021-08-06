# type: ignore
import uvicorn
from fastapi import FastAPI

import settings
from src import base
from src.proxy import aiohttp, httpx

app = FastAPI(debug=settings.DEBUG)

app.include_router(aiohttp.router)
app.include_router(httpx.router)
app.include_router(base.router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
        workers=1,
    )


