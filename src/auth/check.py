from fastapi import responses, status

from . import user_control

print('sdf')

def check_auth(func):
    def wrapper(*args, **kwargs):
        print("SSSSSSSSSSSSdsdS")
        print(args)
        print(kwargs)
        print("SSSSSSSSSSSSS")
        if user_control.is_user_master(args[1]):
            func(*args, **kwargs)
        return responses.JSONResponse(status_code=status.HTTP_403_FORBIDDEN,
                                      content={"message": "This method requires authorization. It`s forbidden for you"})
    return wrapper
