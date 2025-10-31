class Bar:
    def __init__(self, name: str, age: int) -> None:
        self.name:str = name
        self.age:int = age

x: int | float = 1 # int or float -> 조합

from typing  import Literal, NoReturn, Union
y:Union[int, float] = 1

# Collection -> expression, type of the elements in a collection
# list, tuple, set, dict

x1:list[int] = [1, 2, 3, 4]
x1 = [2]

y1:tuple[int, str, int, int] = (1, "2", 3, 5)
y1 = (1, "3", 5, 7)

# json파일 다룰때 많이 사용 함
y2:dict[str, str] = {"name": "ss"}

from typing import Optional, Union

# int or None
x2:Optional[int] = 2
x2 = None

def add_user(name:Optional[str])->str | None:
    if name is None:
        raise ValueError("Name Must be values")

    print(name)

# 값의 자료형과 값까지 알려줌, 
def move(direction:Literal["forward", "left","right","backward"])->None:
    ...

move("forward")
move("left")
move("right")
move("backward")

# Function이 first-citizen으로 만들어 질 때
# 변수의 값을 읽고, 데입할 수 있ㅇ면 1급 시민

# close function: capturing, 생명, 참조
def test(): ... # 함수도 하나의 값으로 저장 가능

x = test
x()     # 호출 가능
def run (func):     #반한값으로 처리 하기
    return func

# 1급 시민 -> 가차 기존이 되는 정의 -> 폐쇄 함수 지원
