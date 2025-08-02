from fastapi import FastAPI,Request, HTTPException,Depends
from pydantic import BaseModel
from typing import List,Annotated 


class Room_Booking(BaseModel):
    room_id: int
    user_id: int
    start_time: str
    end_time: str
class Room_Booking_response(BaseModel):
    room_id: int
    user_id: int
    start_time: str
    end_time: str
    status: str