from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(mapas={"title": "Metroid Database", "description": "A database of Metroid games", "version": "1.0.0"} )

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/zero-mission.html", response_class=HTMLResponse)
async def zero_mission(request: Request):
    return templates.TemplateResponse(
        request=request, name="zero-mission.html",
    )


@app.get("/samus-returns.html", response_class=HTMLResponse)
async def samus_returns(request: Request):
    return templates.TemplateResponse(
        request=request, name="samus-returns.html", 
    )


@app.get("/super-metroid.html", response_class=HTMLResponse)
async def super_metroid(request: Request):
    return templates.TemplateResponse(
        request=request, name="super-metroid.html",
    )