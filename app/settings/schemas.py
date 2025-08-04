from pydantic import BaseModel

class Room_Booking(BaseModel):
    room_id : int
    user_id :int
    start_time : str
    end_time : str
class Room_BookingCreate(Room_Booking):
    pass
class Room_BookingResponse(Room_Booking):
    status : str