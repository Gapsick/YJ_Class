# 중복되지 않은 난수 값 3개 생성 (0 ~ 9)
import random

count = 0
rand_list = []
while count < 3:
    rand_value = random.randint(0, 9)
    
    for index in range(count):
        if rand_list[index] == rand_value:
            break
    else:
        rand_list.append(rand_value)
        count += 1

print(rand_list)

##############################################
rand_list = [value for value in range(0, 10)]

for _ in range(7):
    del rand_list[random.randint(0, len(rand_list) - 1)]

print(rand_list)

input_values = (input("입력하세요: "))

input_list = [int(value) for value in input_values.split()]
    
print(input_list)