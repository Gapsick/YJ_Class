def menu():
    print("=" * 20)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print()
    print(f"현 입력 데이터 갯수 : {len(student_score)}")
    print(f"전체 학생 평균 값 : {sum(all_avg)/len(student_score) if len(student_score) >= 1 else 0.0}")
    print("=" * 20)

def input_student_score():
    a = input("학번을 입력하세요\n")
    b = input("이름을 입력하세요\n")
    c = int(input("국어 성적을 입력하세요\n"))
    d = int(input("영어 성적을 입력하세요\n"))
    e = int(input("수학 성적을 입력하세요\n"))
    
    # 총 합계
    sum = c + d + e
    # 평균
    avg = sum / 3
    # 리스트로 정리후 추가
    score = [a, b, c, d, e, sum, avg]
    student_score.append(score)
    # 학생 평균 값을 위해 총 합계 리스트에 추가
    all_avg.append(avg)

def show_student_score():
    # 학생들의 평균값으로 하나의 리스트 작성
    student_avg_list = []
    
    temp = student_avg_list[:]
    for person in range(len(student_score)):
        student_avg_list.append(student_score[person][6])
    
    # 기본 학생의 등급을 1로 설정
    student_grade = [1] * len(student_avg_list)
    
    # 학생들의 평균값을 하나하나 비교해 비교하는 값이 작을 경우 1씩 증가
    for i in range(len(student_avg_list)):
        for j in range(len(student_avg_list)):
            if student_avg_list[i] < student_avg_list[j]:
                student_grade[i] += 1
                
    # 기존의 총 합계 리스트에 등수를 추가
    for i in range(len(student_grade)):
        student_score[i].append(student_grade[i])
    
    # 총 합계 리스트 출력
    for i in range(len(student_score)):
        print(f"[ id : {student_score[i][0]} \tname : {student_score[i][1]} \tkor : {student_score[i][2]} \teng : {student_score[i][3]} \tmath : {student_score[i][4]} \tsum : {student_score[i][5]} \tavg : {student_score[i][6]} \tgrade : {student_score[i][7]} ")

# 변수 정리
student_score = []
input_number = 0
all_avg = []

while input_number != 3:
    
    # menu 출력
    menu()
    
    # input값 입력
    input_number = int(input("1 ~ 3 선택하세용: "))
    print()
    
    # input값이 1일때
    if input_number == 1:
        input_student_score()
    # input값이 2일때
    elif input_number == 2:
        show_student_score()
