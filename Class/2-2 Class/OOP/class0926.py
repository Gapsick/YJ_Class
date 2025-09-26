# # Getter/Setter -> Method
# class A:
#     def __init__(self):
#         self.__age = None
    
#     # getter method
#     @property
#     def age(self):
#         return f"나이는 : {self.__age}"
    
#     # setter method
#     @age.setter
#     def age(self, age):
#         if age < 0:
#             raise ValueError("음수 값 오류")
#         self.__age = age

#     def prt(self):
#         print(self.__age)

# obj = A()
# obj.age = 30
# print(obj.age)
# obj.age = -100

# / : 위치기반 매개변수 전용 -> / 앞까지의 모든 매개변수는 위치기반 인자값으로 할당되어야 된다.
# from typing import Union

# def calculate(x : Union[int, float], y : Union[int, float], /, op = "+"):
#     if op == "+":
#         print(x + y)
#     elif op == "-":
#         print(x - y)
#     else:
#         print("error")

# calculate(2, 3) # 5
# calculate(10, 20, "-")  # -10

# def prt(a, *arg):
#     print(a, arg)

# prt(1)
# prt(1, 2)
# prt(1, 2, 3)

# def prt(**arg):
#     for key, value in arg.items():
#         print(f"{key}, {value}")

# prt(a = 2)
# prt(d = 3, test="ddd")

def prt(a, *b, c = 10, d = 20):
    print(a, b, c, d)

prt(1, 2, 3, 4, c = 5)

