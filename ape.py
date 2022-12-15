from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse
from uvicorn import run

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.get("/docs")
async def get_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/health")
async def get_health():
    return JSONResponse({"status": "OK"})


@app.get("/openapi.json", tags=["documentation"])
async def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="API for API Prometheus Exporter", version="1", routes=app.routes))


if __name__ == "__main__":
    run("ape:app", port=8000, reload=False, workers=1)
