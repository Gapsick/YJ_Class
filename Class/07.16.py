# import random

# # Matrix
# bar = [
#     [
#         [13, 8], [55, 85]
#     ],
#     [
#         [10, 20], [30, 40]
#     ],
#     [
#         [40, 50], [60, 70]
#     ]
# ]
# def get_value(bar):
#     return sum([item for record in bar for item in record])


# # [[13, 8], [55, 85]]
# # [[10, 20], [30, 40]]
# # [[40, 50], [60, 70]]


# result = sorted(bar, key = get_value, reverse = True)

# print(result)



# # result = sorted(bar, key = "항목 간 비교 시 비교 값 정렬 알고리즘", reverse = True)
# # [ [matrix],             [matrix],            [matrix] ]
# # [ [[40, 50], [60, 70]], [[13, 8], [55, 85]], [[10, 20], [30, 40]] ]

bar1 = {"a" : 10, "b" : 20, "f" : 1, "d" : 9}

for item in bar1: # key 값 비교
    print(item)

result = sorted(bar1.values())

print(result) # [1, 9, 10, 20]