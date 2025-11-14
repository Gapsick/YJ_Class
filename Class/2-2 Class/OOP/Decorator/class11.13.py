from typing import Any, Self

# python -> function -> first-class citizen

# # nested function
# def login(func):
    
#     name = "out_func"
#     def in_func(id:int):  # nested Function
#         print(f"in_func: id-> {id} at {name}")

#     return wrapper

# @login

# my_func_1 = out_func()

# my_func_1(1)
# my_func_1(2)



# def login(func):
#     print("before login")
#     func()
#     print("after login")
    
# @login   # 인터프리터가 코드 해석 시 해당 함수(메서드) 호출한다.
# def bar():
#     print("bar")

# @login
# def foo():
#     print("foo")


# class Bar:
#     def __init__(self, name:str) -> None:
#         self._name:str = name
    
#     @property
#     def name(self):
#         return self._name + " 안녕하세요"

#     @name.setter
#     def name(self, value:str):
#         self._name = value


# obj = Bar("kss")
# print(obj.name)

