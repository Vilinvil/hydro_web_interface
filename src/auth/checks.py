from functools import wraps

from fastapi import responses
from fastapi import status

from . import user_control


user_controller = user_control.UserControl()


# In func that was decorated with help master_required there should be positional argument username
def master_required(func):
    @wraps(func)
    def wrapper(*args, username=..., **kwargs):
        print("USER: ", username)
        if user_controller.is_user_master(username):
            return func(*args, **kwargs)
        return responses.JSONResponse(status_code=status.HTTP_403_FORBIDDEN,
                                      content={"message": "This method requires master rights. It`s forbidden for you"})

    return wrapper
