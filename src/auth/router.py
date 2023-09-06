from fastapi import APIRouter
from fastapi import responses
from fastapi import status

from . import checks

router_auth = APIRouter(prefix="/auth", tags=["Auth"])


@router_auth.get("/name_master", tags=["sequential"])
async def name_master():
    if checks.user_controller.is_master_exist():
        return {"message": f"Master username is: {checks.user_controller.get_username()}"}

    return {"message": "Master don`t exist"}


@router_auth.post("/create_master/{username}", tags=["sequential"])
def create_master(username: str):
    if checks.user_controller.try_get_role_master(username):
        return {"message": f"Successfully create master with username: {username}"}

    return responses.JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={
        "message": f"Can`t create master with username: {username} because master already exist"})


@router_auth.post("/remove_master/{username}", tags=["sequential"])
def remove_master(username: str):
    if checks.user_controller.try_remove_role_master(username):
        return {"message": f"Successfully remove master with username: {username}"}

    return responses.JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content={
        "message": f"Can`t remove master with username: {username} because he isn`t master"})
