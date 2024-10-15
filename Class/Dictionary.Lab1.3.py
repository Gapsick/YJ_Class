stu_score_dictionary = {}
menu_num = 0

def menu():
    print("=" * 15)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print("=" * 15)

def stu_put_score():
    stu_num = int(input("학번을 입력하세요\n"))
    
    # 이미 등록된 학생일 경우 break
    if stu_num in stu_score_dictionary:
        print("이미 등록된 학생입니다.")
        return

    stu_name = input("이름을 입력하세요\n")
    stu_kor = int(input("국어 성적을 입력하세요\n"))
    stu_eng = int(input("영어 성적을 입력하세요\n"))
    stu_math = int(input("수학 성적을 입력하세요\n"))
    
    # 합계 및 평균
    sum = stu_kor + stu_eng + stu_math
    avg = sum / 3
    
    # Dictionary 정리
    stu_score_dictionary[stu_num] = {"학번" : stu_num, "이름" : stu_name, "국어" : stu_kor, \
        "영어" : stu_eng, "수학" : stu_math, "합계" : sum, "평균" : avg}
    
def show_stu_score():
    show_num = int(input("학생 목록 출력입니다. 원하시는 학번을 입력해주세요\n"))
    choice_subject = input("원하시는 과목을 선택해주세요. (전체 출력원할시 ""전체"" 입력)\n")

    if choice_subject == "전체":
        for key, value in stu_score_dictionary[show_num].items():
            print(f"{key} : {value}\t", end="")
        print()
        
    else:
        print()
        print(f"{choice_subject}점수 : {stu_score_dictionary[show_num][choice_subject]}점 입니다.")

while menu_num != 3:
    
    # 메뉴 출력
    menu()
    menu_num = int(input("원하시는 메뉴를 골라주세요 (1~3)\n"))
    
    if menu_num == 1:
        stu_put_score()
    elif menu_num == 2:
        show_stu_score()
    else:
        print("잘못된 번호입니다. 다시 입력해주세요.")