from .repositories import FrontJsonRepository
from .repositories import StateJsonRepository
from .constants import DATA_JSON_FILE
from .constants import STATE_JSON_FILE
from .connection_manager import ConnectionManager

front_json_repository = FrontJsonRepository(DATA_JSON_FILE)
state_json_repository = StateJsonRepository(STATE_JSON_FILE)

connect_manager = ConnectionManager()
