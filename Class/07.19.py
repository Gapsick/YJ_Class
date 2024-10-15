# args 값은 1개 또는 2개
# args 값이 1개 이면, args x args 매트릭스를 생성하여 반환
# args 값이 2개 이면, args[0] x args[1] 매트릭스를 생성하여 반환
# 초기값은 1~100사이 랜덤 값으로 설정(중복값 허용)
import random

def get_matrix(*args):
    
    if not(1 <= len(args) <= 2):
        return None

    matrix_row = args[0]
    
    if len(args) == 1:
        matrix_col = args[0]
    else:
        matrix_col = args[1]
    
    data_frame = {
        "num_row" : matrix_row,
        "num_col" : matrix_col,
        "data" : [ [random.randint(1, 100) for _ in range(matrix_col)]\
        for _ in range(matrix_row) ]
    }
    
    data_frame['sum'] = lambda: sum([sum(row) for row in data_frame['data'] ])
    
    
    # bar = [ [random.randint(1, 100) for _ in range(matrix_col)]\
    #     for _ in range(matrix_row) ]

    return data_frame

foo = dict()
foo['a'] = get_matrix(3,2)
foo['b'] = get_matrix(3,2)
foo['c'] = get_matrix(3,2)
foo['d'] = get_matrix(3,2)

result = sorted(foo.items(), key = lambda arg:arg[1]['sum']())

for item in result:
    print(item[1]['sum']())
# foo = get_matrix(3, 2)
# # print(foo['num_row'], "\t", foo['num_col'])
# # print(foo['data'])
# print(foo["sum"]())

# 하나의 데이터가 있는데, 설명하기 위한 데이터가 첨부되어 있음
# 설명하는 데이터를 "meta data" 라고 지칭한다