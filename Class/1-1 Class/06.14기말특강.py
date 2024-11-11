# << ---- Add by YC Jung.
# 중복되지 않은 난수 값 3개 생성 (0 ~ 9)
import random
def get_uni_rand_list(arg_start = 0, arg_end = 10):
    rand_list = [value for value in range(arg_start, arg_end)]

    for _ in range(7):
        del rand_list[random.randint(0, len(rand_list) - 1)]

    return rand_list



rand_list = get_uni_rand_list()

print(f"생성된 난수 값: ", rand_list)

count_trial = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    
    # 사용자로부터 정수 3개 입력
    input_values = (input("입력하세요: "))

    input_list = [int(value) for value in input_values.split()]
    
    # strike, ball 판별
    for i in range(3):
        for j in range(3):
            if rand_list[i] == input_list[j]:
                if i == j:
                    count_strike += 1
                else:
                    count_ball += 1
    
    
    print(f"스트라이크 : {count_strike} 볼 : {count_ball}")    
    
    # strike out 판별
    if count_strike == 0 and count_ball ==0:
        count_strike_out += 1
        print(f"스트라이크 아웃: {count_strike_out} ")

    # 게임종료 조건
    #  -  strike 3개
    if count_strike >= 3:
        print(f"사용자 승리!")
        break
    #  -  strike out 2번
    #  -  시도 횟수가 5번 이상
    if count_strike_out >= 2 or count_trial >= 5:
        print(f"사용자 패배")
        break
    
    count_trial += 1