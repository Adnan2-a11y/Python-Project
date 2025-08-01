from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager

from routers.users import router as user_router
from routers.rooms import router as room_router
from routers.houses import router as house_router


@asynccontextmanager
async def lifespan(app : FastAPI):
    print("Starting up the app...")
    yield
    print("Shutting down the app...")#.\env\Scripts\activate.ps1 

app = FastAPI(title="FastAPI Example",
              description="A simple FastAPI application",
              version="1.0.0",
              lifespan=lifespan )

app.include_router(user_router)
app.include_router(room_router)
app.include_router(house_router)
app.lifespan_context = lifespan


#app.get("/")
#sync def Home():
#   return {"message ": "Hello World!",
#           "author": "Make Curies",
#           "version": "1.0.0",}

#@app.get("/health")
#async def Health_Cheak():
#    return {"Status": "OK"} 

templates = Jinja2Templates(directory = "templates")
@app.get("/",response_class= HTMLResponse)
async def serve_home(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})

