from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import src.mission_control.router as router


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



