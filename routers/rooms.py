from fastapi import APIRouter

router = APIRouter()
@router.get("/rooms")
async def get_rooms():
    return [{"id": 1, "name": "Conference Room A"}, {"id": 2, "name": "Meeting Room B"}]