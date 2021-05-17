import json
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from deta import Deta

import secrets

app = FastAPI()  # create app instance

deta = Deta("")  # provide project key

db = deta.Base("minishort")  # create a DetaBase

app.mount("/static", StaticFiles(directory="static"), name="static")

pages = Jinja2Templates(directory="pages")


@app.get("/")
async def get_home(request: Request):
    return pages.TemplateResponse("index.html", {"request": request})


@app.post("/shorten")
async def shorten_url(url):
    # data = jsonable_encoder(url)
    db.put(url, key=url)
    return {"url": secrets.token_urlsafe(6)}


@app.get("/{url}")
async def redirect_to_(url):
    red_ = db.get(url)
    return RedirectResponse(red_)
