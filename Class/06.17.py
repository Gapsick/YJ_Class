# # Lab 1
# def print_hello():
#     print("Hello, World!")

# print_hello()


# # Lab 2
# def sum_numbers(a, b):
#     c = a + b
#     return c

# print(sum_numbers(3, 5))

# # Lab 3
# def greet_user(name):
#     print(f"Hello, {name}!")

# greet_user('Alice')


# # Lab 4
# def max_of_three(a, b, c):
#     d = 0
#     e = [a, b, c]
    
#     for i in e:
#         if i > d:
#             d = i

#     return d
        
# print(max_of_three(10, 20, 15))


# # Lab 5
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(is_even(4))
# print(is_even(5))

    
# # Lab 6
# def wrap_in_tag(tag, content):
#     a = (f"<{tag}>{content}</{tag}>")
#     return a

# print(wrap_in_tag('p', 'hello'))
# print(wrap_in_tag('b', 'world'))


# # Lab 7
# def contains(lst, target):
    
#     for i in lst:
#         if i == target:
#             return True
#     else:
#         return False

# print(contains([1, 2, 3, 4], 3))
# print(contains([1, 2, 3, 4], 8))


# # Lab 8
# def calculate_average(*args):
#     sum = 0
#     avg = 0
    
#     for i in args:
#         sum += i
    
#     avg = sum / len(args)
#     return avg

# print(calculate_average(1, 2, 3, 4, 5))
# print(calculate_average(6, 7, 8))
# print(calculate_average(10, 20))


# 철문 9
def get_check_digit(arg_ssid):
    #weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    weight = [(value % 8) + 2 for value in range(12)]
    
    ssid = [int(value) for value in arg_ssid]
    
    sum_values = sum([ssid[index] * weight[index] for index in range(12)])
    
    return (11 - sum_values % 11) % 10
    

# 유효한 주민번호 -> True else False
def is_valid_ssid(arg_ssid):
    
    arg_ssid = arg_ssid.replace("-", "")
    
    if len(arg_ssid) != 13:
        return False
    
    # 체크값 계산 알고리즘 구현 필요
    check_digit = get_check_digit(arg_ssid[:]) 
    
    if check_digit == int(arg_ssid[-1]):
        return True
    else:
        return False

print(is_valid_ssid("650212-2871727"))