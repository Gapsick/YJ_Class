# def bar():...


# def test():
#     print("a")
#     yield 1
#     print("b")
#     print("c")
#     yield 2
#     print("d")
#     yield 3
#     print("e")

# obj = test()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())




# Iteration : 순회
# from typing import Sequence

# class MyDataset:
#     def __init__(self, data: Sequence[int]) -> None:
#         self.data = data

#     def __iter__(self):
#         return BarIterator(self.data)       # 호출할때 마다 매번 새로운 Iterator 객체를 만듬


# class BarIterator:
#     def __init__(self, data: Sequence) -> None:     # 매 순회마다 현재 인덱스에 해당하는 값을 반환, 더 이상 순회 요소가 X -> raise StopIteration
#         self.data = data
#         self.index = 0

#     def __next__(self) -> int:
#         if self.index < len(self.data):
#             value = self.data[self.index]
#             self.index += 1
#             return value
#         raise StopIteration
class MyDataset:
    def __init__(self, feature:list, label:list) -> None:
        self.feature:list = feature
        self.label:list = label
    
    def __iter__(self):
        for x, y in zip(self.feature, self.label):
            yield x, y


dataset = MyDataset([1, 2, 3], [10, 20, 30])

for x, y in dataset:
    print("X, Y: {X}, {Y}")