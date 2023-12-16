import logging
import random

from fastapi import FastAPI

app = FastAPI()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/{zip_code}/{last_name}/{first_name}")
def get_naughty_or_nice(zip_code: str, first_name: str, last_name: str) -> str:
    naughty_or_nice = "naughty" if random.randint(0, 1) else "nice"
    logger.info("%s %s from %s is %s", first_name, last_name, zip_code, naughty_or_nice)
    return naughty_or_nice
