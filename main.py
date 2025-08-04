from fastapi import FastAPI, Depends
from routers.room_booking import router as room_booking_router
from sqlalchemy.orm import Session
from app.settings.database import get_db, engine
from app.settings.model import RoomBookingModel, Base

app = FastAPI(title="First Web app", version="0.1.0")
app.include_router(room_booking_router)

Base.metadata.create_all(bind=engine)

