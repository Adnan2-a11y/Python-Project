from fastapi import APIRouter

router = APIRouter()
@router.get("/houses")
async def get_houses():
    return [{"id": 1, "name": "House A"}, {"id": 2, "name": "House B"}]