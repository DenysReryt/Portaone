from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import uvicorn
from app.main import unique_letter

app = FastAPI()

templates = Jinja2Templates(directory='templates/')


@app.get('/', response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/postdata/', response_class=HTMLResponse)
async def postdata(request: Request, text: str = Form(default='')):
    result = unique_letter(text)
    if result is not None:
        return templates.TemplateResponse('data.html', {'request': request, 'result': result})
    else:
        return templates.TemplateResponse('data.html', {'request': request, 'result': 'No unique letter was found'})


if __name__ == '__main__':
    uvicorn.run('app:app', host='localhost', reload=True, port=8000)
