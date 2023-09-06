import random
import asyncio

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from starlette.websockets import WebSocketState
from websockets.exceptions import ConnectionClosedError
from websockets.exceptions import ConnectionClosed

from src.mission_control import router
from src.mission_control.constants import PERIOD_SENDING_PARAMETERS

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
            try:
                await connection.send_text(message)
            except ConnectionClosed as e:
                await connection.close(1000, "All ok")
                self._active_connections.remove(connection)


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def ws_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket)
    try:
        while websocket.application_state is WebSocketState.CONNECTED:
            await asyncio.sleep(PERIOD_SENDING_PARAMETERS)
            rand_int = random.randint(0, 100)
            await manager.broadcast(f"{username} send message: {rand_int}")

    except (WebSocketDisconnect, ConnectionClosed) as e:
        print(f"handle disconnect {username}. With error {e}")
        manager.disconnect(websocket)
        return
