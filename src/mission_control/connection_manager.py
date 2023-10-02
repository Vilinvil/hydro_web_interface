from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self._active_connections: list[WebSocket] = []

    def exist_connections(self) -> bool:
        return bool(self._active_connections)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self._active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self._active_connections.remove(websocket)

    async def send_message(self, message: dict, websocket: WebSocket):
        await websocket.send_json(message)
