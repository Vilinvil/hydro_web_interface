import asyncio
import os
import random
import sys
import time
import websockets
# from starlette.websockets import WebSocketState
import asyncio

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from websockets.exceptions import ConnectionClosedOK

# sys.path.append(os.path.join(sys.path[0], 'src'))
from .mission_control import router
from .mission_control.constants import PERIOD_SENDING_PARAMETERS

app = FastAPI(
    title="Hydro web interface"
)

app.include_router(router.src.auth.router.router_auth)
app.include_router(router.router_mission_control)


# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:9000",
#     "http://0.0.0.0:9000",
# ]

# app.add_middleware(
#     # CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

class ConnectionManager:
    def __init__(self):
        self._active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self._active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self._active_connections.remove(websocket)

    async def send_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self._active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def ws_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    try:
        while True:
            await asyncio.sleep(PERIOD_SENDING_PARAMETERS)
            rand_int = random.randint(0, 100)
            await manager.broadcast(f"{username} send message: {rand_int}")

    except WebSocketDisconnect or ConnectionClosedOK as e: # BaseException as ex TODO why not worked now and BaseExeption work correctly
        manager.disconnect(websocket)
        await manager.broadcast(f"Client {username} disconnect")
