import json
import weakref

from . import utils
from .enumerations import StatusMission

# Maybe need change on environment variable
DATA_JSON_FILE = "data_storage/data.json"
STATE_JSON_FILE = "data_storage/state.json"


class JsonRepository:
    def __init__(self, filename: str):
        self.filename_ = filename
        try:
            with open(filename) as file_:
                self.data_ = json.load(file_)
        except BaseException as er:
            print(f"Exception in __init__ JsonRepository in file: {self.filename_} Exception is:  {er}")

        self._finalizer = weakref.finalize(self, self.exit_)

    def exit_(self):
        with open(self.filename_, "w") as file_:
            try:
                json.dump(self.data_, file_)
                print(f"successfully done with: {self.filename_}")
            except BaseException as er:
                # TODO
                print(f"Exception in exit_ JsonRepository in file: {self.filename_} Exception is:  {er}")


class FrontJson(JsonRepository):
    def __init__(self, filename: str):
        super().__init__(filename)

    def get_data(self) -> dict:
        return self.data_[:]

    def set_data(self, data: dict):
        self.data_ = data

    def get_nodes(self) -> list:
        return self.data_[0].get("nodes", [])

    def get_edges(self) -> list:
        return self.data_[0].get("edges", [])


class StateJson(JsonRepository):
    def __init__(self, filename: str):
        super().__init__(filename)

    def __set_status(self, status_: str):
        if utils.is_exist_in_enum(StatusMission, status_):
            self.data_["status"] = status_
        else:
            raise ValueError(f"status not exist in StatusMission. Your status: {status_}")

    def set_start(self):
        self.__set_status("START")

    def set_stop(self):
        self.__set_status("STOP")

    def set_pause(self):
        self.__set_status("PAUSE")
