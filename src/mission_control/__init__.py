from .repositories import FrontJson
from .repositories import StateJson
from .constants import DATA_JSON_FILE
from .constants import STATE_JSON_FILE

frontJson = FrontJson(DATA_JSON_FILE)
stateJson = StateJson(STATE_JSON_FILE)