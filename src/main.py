import asyncio

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from websockets.exceptions import ConnectionClosed
from fastapi.middleware.cors import CORSMiddleware

from src.mission_control import router
from src.mission_control.constants import PERIOD_SENDING_PARAMETERS
from src.mission_control import connect_manager

app = FastAPI(
    title="Hydro web interface"
)

app.include_router(router.src.auth.router.router_auth)
app.include_router(router.router_mission_control)


origins = [
    "http://0.0.0.0:9000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Access-Control-Allow-Origin", "Access-Control-Request-Headers", "Access-Control-Allow-Methods"],
)


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await connect_manager.connect(websocket)
    while True:
        try:
            await connect_manager.send_message(router.stateJson.data_, websocket)
        except (WebSocketDisconnect, ConnectionClosed) as e:
            print(f"Error: {e} in websocket {websocket}")
            connect_manager.disconnect(websocket)
            return
        await asyncio.sleep(PERIOD_SENDING_PARAMETERS)
