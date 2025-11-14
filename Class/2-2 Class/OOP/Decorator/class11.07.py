from typing import Any, Self

def decorator(func):
    def wrapper(msg:str):
        print("decorator")
        func(msg)
        return wrapper


@decorator  # decorator(test)
def test(msg):
    print("msg")

print("test.__name__")