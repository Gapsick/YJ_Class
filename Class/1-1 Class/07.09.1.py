import os # os 모듈을 임포트

# 현재 Working Directory 경로를 가져와서 'msg 변수에 저장
msg = os.getcwd()
print(type(msg), msg) # 타입 <class 'str'>, 값은 현재 디렉토리의 경로

# 현재 디렉토리의 파일 및 하위 디렉토리 목록을 가져와 'msg' 변수에 저장
msg = os.listdir()
print(type(msg), msg) # 타입 <class 'list'>, 값은 디렉토리 내의 항목 목록

# 현재 디렉토리에 'kin' 이라는 이름의 새로운 디렉토리를 생성
os.mkdir("kin")

# 현재 작업 디렉토리를 방금 생성된 'kin' 디렉토리로 변경
os.chdir("kin")

# 현재 Working Directory 경로를 가져와서 'msg' 변수에 저장
msg = os.getcwd()
print(type(msg), msg) # 이제 경로는 'kin' 디렉토리를 포함한 경로가 된다