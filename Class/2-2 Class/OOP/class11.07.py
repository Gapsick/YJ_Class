from multiprocessing import Value
from typing import Any, Self
from dataclasses import asdict, dataclass, field

# class Bar:
#     def __init__(self) -> None:
#         self.tag = "Bar"   # 1) name: name, value: Bar
    
#     # event -> 객체 멤버 변수에 값을 넣을 때
#     def __setattr__(self, name: str, value: Any) -> None:
#         object.__setattr__(self, name, value)
#         print(f"name: {name}, value: {value}")
    
#     def __getattribute__(self, name: str) -> Any:
#         try:
#             value = object.__getattribute__(self, name)
#             print(f"Get: {name}")
#             return value
#         except AttributeError:
#             print(f"MISSING: {name}")


# obj = Bar()

# print(obj.tag)  # Get: tag


# class Module:
#     def __init__(self)      

# from typing import Any, Self

# class Cal:
#     def __enter__(self)->Self:
#         print("Bar: enter")
#         return self
    
#     def div(self, x, y)->float:
#         return x / y

#     def __exit__(self, exec_type, exec_value, trackback)->bool:     # exec -> exception
#         print(f"exit: type [{exec_type}], val: [{exec_value}],\
#             trace: [{trackback}]")
#         return False


# with Cal() as obj:  # Context manager
#     obj.div(2, 0)

# # Bar: enter
# # ----
# # Bar: exit

@dataclass(order=True)
class Student:  # data 저장용 클래스가 된다.
    id:str      # instance member variable
    name:str  = field(compare = False, repr=False)    # instance member variable
    age:int     # instance member variable
    

std1 = Student("124", "kim", 20)
std2 = Student("124", "lee", 30)

print(std1)
print(std2.name, std2.id, std2.age)
print(asdict(std1))
print(std1 <= std2)



