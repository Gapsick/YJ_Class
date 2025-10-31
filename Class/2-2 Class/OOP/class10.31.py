# class Student:
#     def __init__(self, id:int) -> None:
#         self.id:int = id
#         self.kor:int = 0
#         self.eng:int = 0
#         self.math:int = 0
        
    
#     def __call__(self, kor:int, eng:int, math:int):
#         self.kor = kor
#         self.eng = eng
#         self.math = math
    
#     def __str__(self):
#         return f"Kor: {self.kor}, Math: {self.math}, Eng: {self.eng}"
    
#     def __eq__(self, value: "Student") -> bool:
#         return self.id ==value.id
    

# obj = Student(1)
# obj(10, 20, 30)

# print(obj)


# Iteration : 순회
from typing import Sequence

class Bar:
    def __init__(self, data: Sequence[int]) -> None:
        self.data = data

    def __iter__(self):
        return BarIterator(self.data)       # 호출할때 마다 매번 새로운 Iterator 객체를 만듬


class BarIterator:
    def __init__(self, data: Sequence) -> None:     # 매 순회마다 현재 인덱스에 해당하는 값을 반환, 더 이상 순회 요소가 X -> raise StopIteration
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        raise StopIteration


obj = Bar([1, 2, 3, 4])

for v in obj:
    print(v)  # 1, 2, 3, 4

for v in obj:
    print(v)  # 1, 2, 3, 4








# x = [10, 20, 30]

# for _ in x:
#     print(_)

# foo = iter(x)
# while True:
#     try:
#         print(next(foo))
#     except StopIteration:
#         break