from fastapi import APIRouter
from fastapi import status

from . import frontJson
from . import stateJson
import src.auth.router
from .enumerations import UserRole

router_mission_control = APIRouter(prefix="/mc", tags=["Mission_control"])


@router_mission_control.get("/init", status_code=status.HTTP_200_OK, tags=["sequential"])
async def init(username: str=...):
    return {"role": UserRole.observer, "data": frontJson.get_data()}


@router_mission_control.post("/start", tags=["sequential"])
@src.auth.router.checks.master_required
def start(username: str=...):
    stateJson.set_start()
    return {"message": "Successfully START"}


@router_mission_control.post("/stop", tags=["sequential"])
@src.auth.router.checks.master_required
def stop(username: str=...):
    stateJson.set_stop()
    return {"message": "Successfully STOP"}


@router_mission_control.post("/pause", tags=["sequential"])
@src.auth.router.checks.master_required
def pause(username: str=...):
    stateJson.set_pause()
    return {"message": "Successfully PAUSE"}


@router_mission_control.post('/update', tags=["sequential"])
@src.auth.router.checks.master_required
def update(data: dict, username: str=...):
    frontJson.set_data(data)
    return {"message": "Successfully UPDATE"}
