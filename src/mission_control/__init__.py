from . import repositories


frontJson = repositories.FrontJson(repositories.DATA_JSON_FILE)
stateJson = repositories.StateJson(repositories.STATE_JSON_FILE)