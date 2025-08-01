from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import Jinja2Templates
from routers.users import router as users 
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app :FastAPI):
    print("Starting up the app...")
    yield
    print("Shutting down the app...")

app = FastAPI(lifespan=lifespan)
app.include_router(users)

#@app.get("/")
#async def read_root():
#    return {"message": "Hello, World!"}
templates=Jinja2Templates(directory = "")