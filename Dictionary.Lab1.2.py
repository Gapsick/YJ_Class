# 변수 정의
stu_dictionary = {}
input_num = 0
avg_list = []

# 1. menu
def menu():
    print("=" * 15)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print()
    print(f"현 입력데이터 갯수 : {len(stu_dictionary)}")
    print(f"전체 학생 평균 값 : {sum(avg_list) / len(stu_dictionary) if len(stu_dictionary) > 0 else 0.0}")
    print("=" * 15)

# 2. 학생 정보 입력
def put_score():
    
    # 학생의 정보 입력
    stu_num = int(input("학번을 입력하세요: "))
    stu_name = input("이름을 입력하세요: ")
    stu_kor = int(input("국어 성적을 입력하세요: "))
    stu_eng = int(input("영어 성적을 입력하세요: "))
    stu_math = int(input("수학 성적을 입력하세요: "))
    
    # 평균값 계산
    sum = stu_kor + stu_eng + stu_math
    avg = sum / 3
    
    # 평균값 리스트에 추가
    avg_list.append(avg)
    
    stu_dictionary[stu_num] = [stu_num, stu_name, stu_kor, stu_eng, stu_math, sum, avg]
    
    return stu_dictionary
    
# 3. 학생 정보 출력
def show_stu_score():
    find_stu_num = int(input("찾고 싶은 학생의 학번을 입력하세요: "))
    a = stu_dictionary[find_stu_num]
    print(f"id :{a[0]} \tname : {a[1]} \tkor : {a[2]} \teng : {a[3]}\
        \tmath : {a[4]} \tsum : {a[5]} \tavg : {a[6]}")
        
# 실행
while input_num != 3: # 3번 종료
    
    # menu 실행
    menu()
    input_num = int(input("원하시는 번호를 선택하세요 (1~3): "))
    
    # 1번
    if input_num == 1:
        put_score()
    # 2번
    elif input_num == 2:
        show_stu_score()
    # 1, 2, 3이 아닐경우
    else:
        print("잘못 입력하셨습니다. 다시 입력해 주세요")

    print()