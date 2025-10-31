# def test(x:int, y:float, z:str)->str:
#     return f"{x}, {y}, {z}"

# import string
# from typing import Callable

# # my_func -> argument -> 3개, 반환형은 문자열
# # Callable[매개변수 자료형, 반환값 자료형]

# # Callable[[매개변수1 자료형, 매개변수2 자료형...], 반환값 자료형]

# def run(my_func:Callable[[int, float, str],str], a:int, b:float, c:str)->None:
#     print(my_func(a, b, c))

# # test 함수를 run 함수의 매개변수에 할당
# run(test)

# def test_2(x, y):
#     ...

# run(test_2)

# TypedDic -> 스키마 정의 -> dictionary -> JSON
# from typing import TypedDict, NamedTuple

# class User(TypedDict):
#     name:str
#     age:int
#     gender:str

# x:User = {"name": "sskim", "age": 20, "gender": "M"}

# x = {"name": "ssskim", "age": 25, "gender": "M"}

# # ------------------------
# from typing import NamedTuple

# class User1(NamedTuple):
#     name:str
#     age:int
#     gender:str

# u1 = User1("ycjung", 2, "M")

# def create_user(name:str, age:int, gender: str) -> User1:
#     return User1(name, age, gender)

# name, age, gender = create_user("ycjung", 2, "M")

# # Magic Method

# print(1+2)
# print( (1).__add__(2))

class Vector:
    def __init__(self, x:int, y: int)->None:
        self.x:int = x
        self.y:int = y

    def __add__(self, r_operand:"Vector"):
        x = self.x + r_operand.x
        y = self.y + r_operand.y

        return Vector(x,y)
    
    
v1 = Vector(1, 2)
v2 = Vector(3, 4)


v3 = v1 + v2    # v3 = v1.__add__(v2)

print(v3.x, v3.y)

v4 = v1 + v2

# x3 = v1.x + v2.x
# y3 = v1.y + v2.y

# v3 = Vector(x3, y3)






