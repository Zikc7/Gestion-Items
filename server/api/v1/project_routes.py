from fastapi import APIRouter

router = APIRouter(prefix="/Items")

@router.get("/") #? /projects/
async def get_all():
    return []