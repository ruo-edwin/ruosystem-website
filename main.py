from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


@app.get("/blog/best-pos-system-for-retail-shops-in-kenya")
async def article(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="bestpossystem.html",
        context={}
    )