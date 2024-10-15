# 사용자로부터 행과 열의 수를 입력 받아, 해당 크기에 맞는 2차원 리스트를 생성
# 사용자는 각 요소에 들어갈 값을 직접 입력하고,
# 입력이 완료되면 완성된 2차원 리스트를 출력

# rows, cols 수 입력 받기
user_input_rows = int(input("Enter the number of rows: "))
user_input_colums = int(input("Enter the number of columns: "))

# 2차원 리스트 생성
matrix = [[0 for _ in range(user_input_colums)] for _ in range(user_input_rows)]

# 리스트 값 입력
for i in range(user_input_rows):
    for j in range(user_input_colums):
        matrix[i][j] = int(input(f"Enter value for [{i}][{j}]: "))

# 리스트 출력
for row in matrix:
    for colums in row:
        print(colums, end = " ")
    print()