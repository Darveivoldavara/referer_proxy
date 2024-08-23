import logging
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()

@app.get("/redirect_to_bot")
async def redirect_to_bot(request: Request):
    try:
        referer = request.headers.get("Referer", "Unknown")

        logger.info(f"{datetime.now()}: Referer: {referer}")

        return RedirectResponse(
            url=f"https://t.me/IcebergCustomerBot?start={referer}"
        )
    except Exception as e:
        logger.error(f"{datetime.now()}: {e}")
        return