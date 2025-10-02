# from typing import Union

# x = "1.0"      # int    # float

# if isinstance(x, int):
#     print(f"x int: {type(x)}")
# elif isinstance(x, float):
#     print(f"x float: {type(x)}")
# else:
#     raise TypeError("unsupported tape")

from functools import singledispatch

# 매개변수 1개 -> 오버로딩 구현
# 지원 자료형은 int, float

@singledispatch
def bar(x):
    raise TypeError("unsupported type")

# @bar.register(float)
# def _(x : float):
#     print("float")

# @bar.register(int)
# def _(x : int):
#     print("int")

bar(2)

from abc import ABC, abstractmethod

# 추상 클래스를 정의
# Java -> abstract class Bar{ }

# Bar를 추상클래스로 정의
class Bar(ABC):
    
    
    # 추상 인스턴스 메서드 정의
    @abstractmethod
    def instance_method(self):
        pass

class MyClass(Bar):
    def instance_method(self):
        print("MyClass : instance_method")
    
    
obj = Bar()
obj.instance_method()