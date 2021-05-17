import json
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel
import secrets

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

pages = Jinja2Templates(directory="pages")


class URLModel(BaseModel):
    url: dict


@app.get("/")
async def get_home(request: Request):
    return pages.TemplateResponse("index.html", {"request": request})


@app.post("/shorten")
async def shorten_url(url):
    # data = jsonable_encoder(url)
    return {"url": secrets.token_urlsafe(6)}
