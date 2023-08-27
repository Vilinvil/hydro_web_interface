from enum import Enum


def is_exist_in_enum(enumeration: Enum, value) -> bool:
    for i in enumeration:
        if i.value == value:
            return True

    return False
