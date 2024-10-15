bar = {
    "ycj" : {"name" : "정영철", "age" : 20},
    "lny" : {"name" : "이나영", "age" : 30}
    }

foo = [d for d in bar.values()]

print(foo)







# foo = [[g for g in range(2)] for value in range(3)]

# for g in range(2):
#     for value in range(3):
#         value

# print(foo)


# stu_grades = {} # Dictionary

#                      이름   국어 영어 수학 총점 평균
# stu_grades[240001] = ["홍길동", 10, 20, 30, 60, 30]
# stu_grades[240002] = ["홍길삼", 100, 200, 300, 600, 300]
# stu_grades[240003] = ["홍길사", 1000, 2000, 3000, 6000, 3000]
# stu_grades[240004] = ["홍길오", {"국어": 100, "수학": 20, "영어" : 10}]
# print(sum(stu_grades[240004][1].values()))


# bar = {
#     "ycj" : {"name" : "정영철", "age" : 20},
#     "lny" : {"name" : "이나영", "age" : 30}
# }

# for item in bar.values():
#     for e in item.values():
#         print(e)

# keys()    : 키 값
# values()  : 데이터 값
# items()   : 키 + 데이터

# print(bar.items())


# for key, value in bar.items():
#     print(key, "\t", value)
    
# for key in bar.keys():
#     print(key, "\t", bar[key])
    
    



# sum = 0
# for record in bar.values():
#     sum += record

# print(sum(bar.values())) # sum([20, 30, 40])

# bar['email'] = "kim@naver.com"

# age가 있으면 Skip하고 없으면 추가해라.

# if "email" in bar: # ['name', 'age', 'phone']
#     print("True")
# else:
#     print("False")
    
# if "mobile" in bar.keys(): # ['name', 'age', 'phone']
#     print("True")
# else:
#     print("False")
