# bar = [1, 2, 3, 4]

# print(bar.pop(2))

# print(bar)

# # 3
# # [1, 2, 4]

# bar = [10, 20, 30, 40]

# while len(bar) > 0:
#     item = bar.pop(0)
#     print(item)

# # 10
# # 20
# # 30
# # 40


def menu():
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print()
    print(f"현 입력 데이터 갯수 : {len(student_score)}")
    print(f"전체 학생 평균 값 : ")

def input_student_score():
    a = input("학번을 입력하세요\n")
    b = input("이름을 입력하세요\n")
    c = input("국어 성적을 입력하세요\n")
    d = input("영어 성적을 입력하세요\n")
    e = input("수학 성적을 입력하세요\n")
    
    score = [a, b, c, d, e]

    student_score.append(score)

def show_student_score():
    pass    


student_score = []

while input_number != 3:
    # menu 출력
    menu()
    
    # input값 입력
    input_number = int(input("1 ~ 3 선택하세용: "))
    
    # input값이 1일때
    if input_number == 1:
        input_student_score
        
    # input값이 2일때
    elif input_number == 2:
        pass
    
    
    # input값이 3일때
    elif input_number == 3:
        break
    
