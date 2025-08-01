from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routers.users import router as user

app = FastAPI(title ="Make Curies")
templates = Jinja2Templates(directory = "templates")
@app.get("/",response_class = HTMLResponse)
async def user_home(request : Request):
    return templates.TemplateResponse("user.html",{"request":request})
#@app.get("/")
#async def home():
#    return {"Message":"Welcome to Make Curies!"}
app.include_router(user)
