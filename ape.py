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
    "query_delay": 3,
    "port": 8000,
})
cached_metric_registry = CollectorRegistry()


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
    return Response(generate_latest(cached_metric_registry))


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(update_metrics_task())


async def update_metrics_task():
    global cached_metric_registry
    counter = 0  # LATER Remove counter used for debugging.
    while True:
        print(counter)
        cached_metric_registry = await update_metrics(counter)
        counter += 1
        await asyncio.sleep(config["query_delay"])


# TODO Move to a separate file.
async def update_metrics(counter: int) -> CollectorRegistry:
    registry = CollectorRegistry()
    g = Gauge('my_first_gauge', 'will increment', registry=registry)
    g.set(counter)
    g2 = Gauge('my_second_gauge', 'will always be 2', registry=registry)
    g2.set(2)
    return registry


if __name__ == "__main__":
    run("ape:app", port=config["port"], reload=False, workers=1)
