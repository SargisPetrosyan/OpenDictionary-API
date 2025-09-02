from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services import get_word

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get('/home/', response_class=HTMLResponse)
async def redirect_home_v2(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get('/api/words/en/{word}/',)
async def get_definitions(word:str):
    return await get_word(word=word)

