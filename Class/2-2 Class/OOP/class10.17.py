# def div(x: int | float, y: int | float)->float:
#     return x / y

# print(div(4, 2))    # 2.0
# print(div("4", "2"))    # error

# a: None = None

# Callable(param...) -> return type
# def sum(x :int, y: int)->int:
#     return x + y

# class Bar:
#     def __init__(self, x: int, y: str) -> None:
#         self.x:int = x
#         self.y:str = y

# def something(a: int, b: float, c:None=None)->None:
#     ...

# # Collection -> Abstract Data Type -> Implementation Set
# # Python -> list, tuple, dict, set

# x: list = [1, 2, 3]

# x = (1, 2, 3)
# x = {1, 2, 3}
# x = {1:2, 3:4, 5:6}

# from typing import List
# y:List = [1, 2, 3, 4]   # Legacy


# def get_total_avg(x: int, y:int)->tuple:
#     sum = x + y
#     avg = sum / 2
#     return sum, avg

# x_tuple:tuple = (1, 2, 3)

# x_tuple = [1, 2, 3]

# x_dict:dict = {1:2, 3:4}

# x_set:set = {1, 2, 3}

# x_range:range = range(2)


# x_list_int:list[int | float] = [1, 2, 3]
# x_list_int = ["2", 3, 4.0]

# # Tuple은 갯수와 자료형이 일치 해야함
# x_tuple_int:tuple[int float, str, int] = (2, 2.0, "2", 4)

# y:tuple[int, ...]
# y = (1, 2, 3)
# y = (2, 3, 4, 5, 6)

# x_dic_str_float:dict[str, float] = {"k1":2.0, "k2":3.0}
# x_dic_str_float = {1:2.0}

# x_set_bool:set[bool] = {True, False}

# from typing import Sequence

# # Sequence -> Type hinting -> list, tuple, range
# x_seq_int:Sequence[int] = [1, 2, 3]
# x_seq_int = (1, 2, 3)
# x_seq_int = {1, 2, 3}
# x_seq_int = {1:2, 3:4}

# Union -> 집합의 원소 중 하나이면 -> OK, 모두 해당되지 않으면 -> Error

# from typing import Union

# x: Union[int, float, bool]
# x_new:int | float | bool

# x = 2
# x = 3.0
# x = False
# x = "2"     # Error

# Optional -> if else -> if [T] else None

# from typing import Optional

# x_op_int: Optional[int]

# x_op_int = 3
# x_op_int = None
# x_op_int = "4"

# from typing import Literal
# gender:Literal["man", "woman"]
# gender = "man"
# gender = "woman"
# gender = "1234"

# from typing import Any

# x: Any
# x = 1
# x = 2.0
# x = "d"

# Callable -> 함수, 메서드

# from typing import Callable

# def sum(x: float, y: float)->float:
#     return x + y

# sum_2 = sum
# sum_2(2, 3)     # 5

# def do_something(x: float, y: float, op:Callable[[float, float], float]):
#     return op(x, y)

# do_something(1, 2, sum)


