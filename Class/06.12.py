# bar = 3

# def foo(bar): # call-by-value
#     bar = bar + 1

# foo(bar)

# print(bar) # 3

# keyword argument
# def pos(arg_a, arg_b, arg_c):
#     print(arg_a, arg_b, arg_c)

# pos(arg_c = 1, arg_a = 2, arg_b = 3)

# default argument
# def kin(arg_a = 1, arg_b = 2, arg_c = 3, arg_d = 4):
#     print(arg_a, arg_b, arg_c, arg_d)

# kin()
# kin(6, 7, 8, 9)
# kin(6)
# kin(6, 7)
# kin(6, 7, arg_d = 10)

# data = [2, 3, 4, 5]

# 구구단을 출력하는 프로그램 작성하시오 : 2단 ~ 9단
# 함수로 작성: printMulTable()
#           1) 2, 3 -> 2단과 3단을 출력
#           2) 3 -> 3단만 출력
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i * j}")

#     print("*********")



def printMulTable(arg_start, arg_end = None):
    
    # if arg_end == None:
    #     arg_end = arg_start
    
    arg_end = arg_start + 1 if arg_end is None else arg_end + 1    
    
    for i in range(arg_start, arg_end):
        for j in range(1, 10) :
            print(f"{i} X {j} = {i * j}")

# printMulTable(2)

        # * -> 가변 : tuple로 받겠다
def foo(*args):
    print(len(args))
    for value in args:
        print(value)

# foo(1, 2, 3, 4, 5, 6, 7, 8, 9) # 9

def bar(*args):
    if len(args) == 1:
        start = end = args[0]
    elif len(args) == 2:
        start, end = args
    else:
        return
    
    for dan in range(start, end + 1):
        for num in range(1, 10):
            print(f"{dan} X {num} = {dan * num}")

# bar(2)

def foo(**args):
    print(len(args))
    
    for key, value in args.items():
        print(f"key : {key}, value : {value}")

# foo(test = 2, king = 3)
# foo(test = 2, king = 3, lion = 4)

def foo (arg_a, arg_b, arg_c, arg_d, arg_e):
    print(arg_a, arg_b, arg_c, arg_d, arg_e)

# foo (1, 2, 3, 4, 5)

arg_list = [value for value in range(1, 6)]
arg_list = [1, 2, 3, 4, 5]

foo(*arg_list) # Collection unpacking