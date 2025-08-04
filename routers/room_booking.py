from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.settings.schemas import Room_BookingCreate, Room_BookingResponse
from app.settings.crud import Create_room_booking
from app.settings.database import get_db

router = APIRouter()
@router.post("/book_room", response_model= Room_BookingResponse)
async def Book_Room(
    booking: Room_BookingCreate, db: Session = Depends(get_db)
):
    """
    Endpoint to book a room.
    """
    return Create_room_booking(db, booking)