# Dictionary
# bar = {'a' : 10, 'f': 20, 'c' : 5, 'b' : 4}

# bar = lambda x, y :x * y

# print(bar(2,3)) # 6

# def foo(x, y): # 함수이름도 변수처럼 저장이 가능하다.
#     return x * y

# pos = foo # key point (함수의 주소가 저장)
# print(pos(4, 3))

# bar = lambda x, y :x * y 
# # lambda 함수의 특징
# # 1. 함수의 이름 X 
# # 2. 콜론을 이용해 매개변수 분리  
# # 3. 값이 들어가고 return함   
# # 4. 함수를 하나를 정의 (이 함수의 메모리 주소값이 넘어옴, bar 변수에 저장)

# ############################################
# bar = (x, y) : return x * y
# -> bar = lambda x, y : x * y

# ############################################
# def Anonymous(x, y):
#     return x * y

# bar = Anonymous

bar = [10, 9, 2, 8]

result = sorted(bar, reverse = True)

print(result) # [10, 9, 8, 2] 내림차순 정렬

result = sorted(bar, reverse = False)

print(result) # [2, 8, 9, 10] 오름차순 정렬

bar = [[10, 9],
       [2, 8],
       [3, 10]
       ]

# Matrix 일때는 Record 단위로 분류를 한다.

result = sorted(bar, reverse = True)

print(result) # [[10, 9], [3, 10], [2, 8]] 내림차순 정렬

result = sorted(bar, reverse = False)

print(result) # [[2, 8], [3, 10], [10, 9]] 오름차순 정렬

def get_value(record):
    return record[1]

result = sorted(bar, key = get_value, reverse = True)
result = sorted(bar, key = lambda record : record[1], reverse = True)


