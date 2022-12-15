import asyncio
from fastapi import FastAPI, Response
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.responses import JSONResponse
from uvicorn import run
from prometheus_client import CollectorRegistry, Gauge, generate_latest

from configuration import Configuration

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
config = Configuration({
    "port": 8000,
})
cached_metrics = None


@app.get("/docs")
async def get_docs():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/health")
async def get_health():
    return JSONResponse({"status": "OK"})


@app.get("/openapi.json", tags=["documentation"])
async def get_open_api_endpoint():
    return JSONResponse(get_openapi(title="API for API Prometheus Exporter", version="1", routes=app.routes))


@app.get("/metrics")
async def get_metrics():
    global cached_metrics  # TODO Move this assignment to a task running in the background.
    cached_metrics = get_my_metrics()

    return Response(cached_metrics)


# Test out prometheus client and move this to a separate file later.
# TODO Create a background task that generates metrics, updates the cached results, waits, and repeats.
def get_my_metrics() -> bytes:
    registry = CollectorRegistry()
    g = Gauge('my_first_gauge', 'will always be 1', registry=registry)
    g.set(1)
    g2 = Gauge('my_second_gauge', 'will always be 2', registry=registry)
    g2.set(2)
    return generate_latest(registry)


if __name__ == "__main__":
    run("ape:app", port=config["port"], reload=False, workers=1)
