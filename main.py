import logging
import random

from fastapi import FastAPI
from opentelemetry import metrics, trace

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

tracer = trace.get_tracer("tracer")
meter = metrics.get_meter("meter")

counter = meter.create_counter(
    "naughty_or_nice_counter",
    description="The count of naughty and nice",
)


@app.get("/{name}/")
def get_naughty_or_nice(name: str) -> str:
    with tracer.start_as_current_span("get_naughty_or_nice") as span:
        naughty_or_nice = "naughty" if random.randint(0, 1) else "nice"
        span.set_attribute("naughty_or_nice", naughty_or_nice)
        counter.add(1, {"value": naughty_or_nice})
        logger.info("%s %s is %s", name, naughty_or_nice)
        return naughty_or_nice
