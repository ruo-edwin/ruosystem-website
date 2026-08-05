from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sitemap import router as sitemap_router
from robots import router as robots_router


app = FastAPI()


app.include_router(robots_router)
app.include_router(sitemap_router)

# Redirect apex domain to www
@app.middleware("http")
async def redirect_to_www(request: Request, call_next):
    host = request.headers.get("host", "").split(":")[0]

    # Only redirect the apex domain
    if host == "ruosystem.co.ke":
        url = request.url.replace(
            netloc=f"www.{host}",
            scheme="https"
        )
        return RedirectResponse(url=str(url), status_code=301)

    return await call_next(request)


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )


@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={}
    )


@app.get("/blog/best-pos-system-for-retail-shops-in-kenya")
async def article(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="bestpossystem.html",
        context={}
    )


@app.get("/blog")
async def blog(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="blog.html",
        context={}
    )


@app.get("/blog/inventory-management-system-for-retail-shops-in-kenya")
async def article(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="inventorymanagement.html",
        context={}
    )


@app.get("/blog/how-much-does-a-pos-system-cost-in-kenya")
async def article(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="poscostkenya.html",
        context={}
    )