from enum import Enum


class StatusMission(Enum):
    start = "START"
    stop = "STOP"
    pause = "PAUSE"


class UserRole(Enum):
    master = "MASTER"
    observer = "OBSERVER"
