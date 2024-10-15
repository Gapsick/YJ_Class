# Start, End, N의 세 값을 입력 받는다
# 이 값들을 사용하여 Start와 End 사이에서 중복되지 않은 N개의 난수를 생성 후 
# 1차원 리스트에 저장 후 출력하는 프로그램을 작성
import random

# 변수 정의
random_list = []
while True:
    
    # Start 입력
    while True:
        print("난수를 생성할 범위와 개수를 입력하세요.")
        user_input_start = int(input("Start (0 이상의 정수): "))
        if user_input_start > 0:
            break
        print("Start는 0보다 커야 합니다.")
    
    # End 입력
    while True:
        user_input_end = int(input("End (Start보다 큰 정수): "))
        if user_input_end > user_input_start:
            break
        print(f"End는 Start({user_input_start})보다 커야 합니다.")
    
    # N 입력
    while True:
        user_input_N = int(input("N (생성할 난수의 개수): "))
        if 1 <= user_input_N <= 2:
            break
        print("N은 1부터 2 사이의 정수여야 합니다.")
    
    # 값 추가
    for i in range(user_input_N):
        a = random.randint(user_input_start, user_input_end)
        random_list.append(a)
    
    # 출력
    print(f"생성된 난수 리스트: \n{random_list}")
    break