
from functools import wraps
# def is_login(func):
#     def wrapper(msg):
#         print("before")
#         func(msg)
#         print("after")

#     return wrapper     # return : callable

# @is_login   # do_something = is_login(do_something)
# def do_something(msg:str):
#     print(f"do something: {msg}")

# do_something('h1')  # wrapper("h1")
# do_something('h2')  # wrapper("h2")

# def f_a(func):
#     def wrapper():
#         print(f"f_a {func}")
#         func()
#     return wrapper
    
# def f_b(func):
#     def wrapper():
#         print(f"f_b: {func}")
#         func()
#     return wrapper

# @f_a
# @f_b    # bar = f_a(f_b(bar))
# def bar():
#     print("bar")

# bar()

# def strip(func):
#     def wrapper(msg:str):
#         func(msg.strip())
#     return wrapper

# def upper(func):
#     def wrapper(msg:str):
#         func(msg.upper())
#     return wrapper

# @upper
# def prt_something1(msg:str):
#     print(f"prt: {msg}")

# @strip
# def prt_something2(msg:str):
#     print(f"prt: {msg}")

# @upper
# @strip
# def prt_something3(msg:str):
#     print(f"prt: {msg}")

# prt_something1("        test           ")
# prt_something2("        test           ")
# prt_something3("        test           ")

# def upper(func):
#     @wraps(func)
#     def wrapper(msg:str):
#         return func(msg.upper())
#     return wrapper

# @upper
# def bar(msg:str):
#     return msg

# print(bar.__name__)

def test(n):
    def factory(func):
        def wrapper(func):
            func()
        return wrapper
    
    return factory

@test(1)    # test(1) -> factory((bar)) -> bar = factory((bar))
def bar():
    ...

bar()