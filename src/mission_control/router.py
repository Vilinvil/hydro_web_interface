from fastapi import APIRouter
from fastapi import status

from . import frontJson
from . import stateJson

router_mission_control = APIRouter(prefix="/mc", tags=["Mission_control"])


@router_mission_control.get("/init", status_code=status.HTTP_200_OK, tags=["sequential"])
async def init():
    return {"role": "master", "data": frontJson.get_data()}


@router_mission_control.post("/start", tags=["sequential"])
def start():
    stateJson.set_start()
    return {"message": "Successfully START"}


@router_mission_control.post("/stop", tags=["sequential"])
def stop():
    stateJson.set_stop()
    return {"message": "Successfully STOP"}


@router_mission_control.post("/pause", tags=["sequential"])
def pause():
    stateJson.set_pause()
    return {"message": "Successfully PAUSE"}


@router_mission_control.post('/update', tags=["sequential"])
def update(data: dict):
    frontJson.set_data(data)
    return {"message": "Successfully UPDATE"}
