def menu():
    print("=" * 20)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print()
    print(f"현 입력 데이터 갯수 : {len(student_score)}") # 데이터 갯수 = 학생들의 정보의 갯수
    print(f"전체 학생 평균 값 : {sum(all_avg)/len(student_score) if len(student_score) >= 1 else 0.0}") # 학생들의 정보 X -> 평균 0.0
    print("=" * 20)

def input_student_score():
    # 변수명이 암호화 되어 있음
    # 변수명 해독이 필요함
    
    # 학생들의 정보를 입력 받는다.
    num = input("학번을 입력하세요\n")
    name = input("이름을 입력하세요\n")
    korean_s = int(input("국어 성적을 입력하세요\n"))
    english_s = int(input("영어 성적을 입력하세요\n"))
    math_s = int(input("수학 성적을 입력하세요\n"))
    
    # 총 합계
    sum = korean_s + english_s + math_s
    # 평균
    avg = sum / 3
    # 학생들의 정보를 score(list) 로 만든후 student_score에 추가
    score = [num, name, korean_s, english_s, math_s, sum, avg]
    #student_score.append(score)
    
    # Dictionary에 값 추가 key : 학번, value : 학생들의 정보
    student_score_dictionary[f"{num}"] = score
    
    
    # 학생 평균 값을 위해 총 합계 리스트에 추가
    all_avg.append(avg)

def show_student_score():
    student_num = int(input("찾고 싶은 학생의 학번을 입력하세요: "))
    student_inf = student_score_dictionary[f"{student_num}"]
    print(f"[ id : {student_inf[0]} \tname : {student_inf[1]} \
\tkor : {student_inf[2]} \teng : {student_inf[3]} \tmath : {student_inf[4]} \
\tsum : {student_inf[5]} \tavg : {student_inf[6]}")
    print()
    
    
    
# 변수 정리
student_score = [] # 학생들의 정보를 저장하는 List
input_number = 0 # User - menu번호
all_avg = [] # 전체 학생 평균을 알아내기 위한 평균의 총합 리스트
student_score_dictionary = {} # 학생 정보를 기록한 Dictionary

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
