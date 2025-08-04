from sqlalchemy import Column, Integer, String
from app.settings.database import Base

class RoomBookingModel(Base):
    __tablename__ = "room_booking"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    start_time = Column(String, nullable=False)
    end_time = Column(String, nullable=False)
    status = Column(String, default="pending")