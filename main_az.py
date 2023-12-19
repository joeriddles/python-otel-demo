import functools
import os
import random
import time
import typing

from azure.monitor.opentelemetry import configure_azure_monitor
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from opentelemetry import metrics

# See:
# - https://github.com/Azure/azure-sdk-for-python/issues/33301
# - https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/monitor/azure-monitor-opentelemetry#usage
# - https://opentelemetry-python.readthedocs.io/en/latest/sdk/environment_variables.html#opentelemetry.sdk.environment_variables.OTEL_EXPERIMENTAL_RESOURCE_DETECTORS
os.environ["OTEL_EXPERIMENTAL_RESOURCE_DETECTORS"] = "azure_app_service"

# loads from APPLICATIONINSIGHTS_CONNECTION_STRING environment variable
configure_azure_monitor(
    disable_logging=True,
    disable_tracing=True,
)

app = FastAPI()

meter = metrics.get_meter("main")
counter = meter.create_counter("request-count")
histogram = meter.create_histogram("request-latency")


def record_latency(func: typing.Callable) -> typing.Callable:
    """Record how long `func` takes to execute and report its latency."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            duration_ms = (time.time() - start) * 1_000
            histogram.record(duration_ms, kwargs)
            return result
        except Exception as err:
            duration_ms = (time.time() - start) * 1_000
            kwargs["error"] = str(err)
            histogram.record(duration_ms, kwargs)
            raise err

    return wrapper


@app.get("/{name}/")
@record_latency
def get_naughty_or_nice(name: str):
    counter.add(1, {"name": name})

    time.sleep(random.randint(0, 3))  # sleep between 0-3 seconds

    naughty_or_nice = "naughty" if bool(random.randint(0, 1)) else "nice"
    return HTMLResponse(f"{name}, you have been very {naughty_or_nice} this year!")
