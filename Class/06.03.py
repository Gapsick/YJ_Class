# Nested (중첩) : 한 개의 흐름제어문 내에 또 다른 흐름제어문이 존재할 경우
# loop - 3개 : Legacy C언어  Java 언어
#  1) for
#  2) while
#  3) do-while

# 인자값 1개 : 반복의 횟수

# for _ in range (9):
#     print(_, end="")

# print("\n", "*" * 20)

# for dan in range(2, 10):
#     print(dan, end="")
    
# # 반복의 횟수가 다르다

# list comprehension - 리스트 내 원소 값들을 for문을 사용하여 동적으로 생성
# [expression(수식) for item in item_list if conditional expression]
# 동적 : 프로그램이 실행하면서 변화 하는 것
# 수식 : 연산자, 피연산자

# value = int(input("양의 정수를 입력하세용가리: "))
# list_m = [i for i in range (1, value)]
# print(list_m)

# for문의 반복 회수 = 원소의 개수
# for문 앞의 값 = 


# # 1에서 10사이 정수 중, 홀수는 10을 곱하고, 짝수는 20을 곱한 리스트를 생성하라
# a = [value * 20 if value % 2 == 0 else value * 10 for value in range(1, 11)]

# print(a)

# s_list = [value for value in range(1, 21) if value % 3 == 0 and value % 4 == 0]
# print(s_list)

# while
# while 조건식:
#       참 일때 실행되는 문장

# 키보드로부터 정수를 입력 받고, 양수일 경우 출력
# 음수 또는 0인 경우 재입력 -> 양수가 입력 될 때까지

# while True:
#     input_user = int(input("정수를 입력하세요 : "))
    
#     if input_user > 0:
#         print(input_user)
#         break
    
#     else:
#         print("마 똑바로 입력해라")
    
# while 문을 이용하여 1에서 10까지 출력하는 프로그램을 작성하라.

# num = 1
# while True:
#     print(num)
#     num += 1
    
#     if num == 11:
#         break

bar = ["hello", "world", "Richard"]
# found_word = False      # Flag 변수 -> 깃발 : Boolean

for word in bar:
    
    if word == "world":
        print("단어를 찾았음")
        # found_word = True
        break

else: # 반복문이 정상적으로 종료했을때 (횟수가 다됬을경우), # break, return 인 경우 실행 X
    print("단어를 찾지 못했음. 나~~빠~~또")

# else를 왜썼을까? flag 변수를 따로 쓰지 않아도 되기 때문!
