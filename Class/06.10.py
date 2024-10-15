# 정수 3개를 입력 받아 합계와 평균을 출력하는 프로그램을 작성하라.
# def get_sum():
    
#     a, b, c = map(int, input("정수 3개 입력 : ").split())
    
#     sum = a + b + c
#     avg = sum / 3
    
#     print(sum)
#     print(avg)

# get_sum()

# def get_int(arg_num):
#     input_values = []
#     for _ in range(arg_num):
#         input_values.append(int(input("입력값: ")))
    
#     return input_values

# def get_sum_avg(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     avg = sum / len(arg_list)
    
#     return sum, avg

# def get_sum(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     return sum

# input_list = get_int(5)
# sum, avg = get_sum_avg(input_list)
# print(sum, avg)

#########################

# 함수 정의 -> 1번
# def print_name(name):
#     print(name, "님 안녕하세요")

# # 함수 호출 -> 2번
# print_name("리차드")
# print_name("김성식")

# def sum (arg_first, arg_second):
#     sum = arg_first + arg_second
    
#     if sum < 0:
#         print("음수")
#         return # None
    
#     # 함수 정의 시 return 있어도 되고 없어도 된다. 즉 Option 이다
    
#     return sum # 두 가지 role -> 1) 함수 종료 2) 값 반환

# result = sum(2, 3)
# print(result) # result -> 5

# result = sum(-2, -3)
# print(result)

# 함수의 인자 값 4개를 입력 받아 합계와 평균을 반환하는 함수를 작성하라.
# 그리고 반환된 합계와 평균을 화면에 출력하라.

# def calculate(a, b, c, d):
#     sum = a + b + c + d
#     avg = sum % 4
    
#     return sum, avg # 반환값이 두 개 이상이면 tuple로 변환 후 반환한다.

# print(type(calculate(1, 2, 3, 4)))
# sum, avg = calculate(1, 2, 3, 4)

# print(sum, avg)

# Call-by-value, Call-by-reference
# value -> 값이 복사되어 원본 값에 영향 X
# reference -> 값이 복사되는 것이 아니고 원본 주소값을 복사하는것이기 때문에
#              원본 값에 영향을 줌
bar = 3

def foo(bar):
    bar = bar + 1
    print("1: ", bar)

foo(bar)

print("2: ", bar)

