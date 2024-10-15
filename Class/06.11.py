bar = [2, 3, 5]

def foo(arg_list): # 메모리 주소 값
    copied_list = arg_list[:] # Slicing -> 새로운 리스트를 만들고 copied_list(변수)에 메모리 주소 부여
    
    copied_list[0] = 100

foo(bar) # Call-by-reference

print(bar) # 2, 3, 5

def kin(arg_list):
    arg_list[0] = 200
    
    
kin(bar.copy()) # Slicing 과 동일, 새로운 리스트 만들고 메모리 주소를 생성

print(bar)
