class UserControl:
    def __init__(self):
        self.__username = None

    def is_master_exist(self) -> bool:
        return self.__username is not None

    def get_username(self) -> str:
        return self.__username

    def is_user_master(self, username: str) -> bool:
        if username:
            return username == self.__username

        return False

    # try_get_role_master() return True if role_master set
    def try_get_role_master(self, username: str) -> bool:
        if not self.__username:
            self.__username = username
            return True

        return False

    # try_remove_role_master() return True if removing role master successfully
    def try_remove_role_master(self, username: str) -> bool:
        if self.is_user_master(username):
            self.__username = None
            return True

        return False
