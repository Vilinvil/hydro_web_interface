import asyncio

from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
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

    def exist_connections(self) -> bool:
        # return bool(self._active_connections)
        return len(self._active_connections) > 0

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self._active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self._active_connections.remove(websocket)

    async def send_message(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)



manager = ConnectionManager()


@app.websocket("/ws")
async def ws_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    while True:
        try:
            await manager.send_message(router.stateJson.data_, websocket)
        except (WebSocketDisconnect, ConnectionClosed) as e:
            print(f"Error: {e} in websocket {websocket}")
            manager.disconnect(websocket)
            return
        await asyncio.sleep(PERIOD_SENDING_PARAMETERS)
