import os
import sys

from fastapi import FastAPI

sys.path.append(os.path.join(sys.path[0], 'src'))
import auth.router
import mission_control.router

app = FastAPI(
    title="Hydro web interface"
)

app.include_router(auth.router.router_auth)
app.include_router(mission_control.router.router_mission_control)


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



# @app.websocket("/ws")
# async def wsEndpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = get_numbers()
#         await websocket.send_json(
#             {
#                 "course": data[0],
#                 "depth": data[1],
#                 "march": data[2],
#                 "lag": data[3],
#                 "roll": data[4],
#                 "differential": data[5],
#                 "dropper": data[6],
#                 "lifter": data[7],
#                 "global_mission": data[8],
#                 "local_mission": data[9],
#                 "transtion": data[10]
#             }
#         )
#         time.sleep(1)
