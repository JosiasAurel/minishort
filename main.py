from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

pages = Jinja2Templates(directory="pages")


@app.get("/")
async def get_home(request: Request):
    return pages.TemplateResponse("index.html", {"request": request})
