from sqlmodel import Session
from app.settings.model import RoomBookingModel
from app.settings.schemas import Room_BookingCreate

def Create_room_booking(db : Session, booking : Room_BookingCreate):
    db_booking = RoomBookingModel(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
