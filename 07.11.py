### 리터럴을 사용한 생성
my_dict = {'name': 'Alice', 'age': 25}

### 키워드 인자 사용
my_dict1 = dict(name = "Alice", age = 25, Country = "USA")
# 출력: {'name': 'Alice', 'age': 25, 'country': 'USA'}

### 튜플 리스트 사용
pairs = [("name", "Alice"), ("age", 25), ("country", "USA")]
my_dict2 = dict(pairs)
# 출력: {'name': 'Alice', 'age': 25, 'country': 'USA'}

### 키 리스트와 zip 사용
keys = ["name", "age", "country"]
values = ["Alice", 25, "USA"]
my_dict3 = dict(zip(keys, values))
# 출력: {'name': 'Alice', 'age': 25, 'country': 'USA'}


##### Dictionary 사용법 : Read, Update, Delete


# 생성
# 연락처 정보를 저장하는 Dictionary를 생성
# 각 키는 연락처의 속성을 나타내고, 각 값은 해당 속성의 데이터
contact = {
    "name": "John Doe",                     # 이름 필드
    "email": "john.doe@example.com",        # 이메일 필드
    "phone": "123-456-7890"                 # 전화번호 필드
}

### 읽기
# Dictionary에서 각 키를 사용하여 연락처 정보를 읽고 출력.
# print("Name:", contact["name"])      # John Doe
# print("Email:", contact["email"])    # john.doe@example.com
# print("Phone:", contact["phone"])    # 123-456-7890

### 업데이트
# Dictionary key에 새로운 값들을 할당하여 기존의 데이터를 업데이트
contact["email"] = "new.email@example.com"    # 'email' 키의 값을 새 이메일 주소로 업데이트
contact["phone"] = "987-654-3210"             # 'phone' 키의 값을 새 전화번호로 업데이트
contact["address"] = "1234 Main St"           # 새 키 'address'를 추가하고 주소 정보를 할당
# print("\nUpdated:", contact)                  # 업데이트된 전체 딕셔너리를 출력
# 결과 : Updated: {'name': 'John Doe', 'email': 'new.email@example.com', 
# 'phone': '987-654-3210', 'address': '1234 Main St'}

### 삭제
# 'phone' key와 해당 값이 Dictionary에서 삭제
del contact["phone"]
# print("\nDeleted phone:", contact) # 전화번호가 삭제된 후의 딕셔너리를 출력합니다.
# 결과 : Deleted phone: {'name': 'John Doe', 'email': 'new.email@example.com', 'address': '1234 Main St'}

contact.clear() # 모든 키와 해당 값 삭제

##### 순회
person = {
    'name' : 'John',
    'age' : 30,
    'city' : 'New York'
}

### 키와 값을 순회
for key in person:
    print(f'Key: {key}, Value: {person[key]}')
# 결과 : Key: name, Value: John
#        Key: age, Value: 30
#        Key: city, Value: New York

### items() 메서드를 사용한 순회
for key, value in person.items():
    print(f'Key: {key}, Value: {value}')
# 결과 : Key: name, Value: John
#        Key: age, Value: 30
#        Key: city, Value: New York

### keys() 메서드를 사용한 순회
for key in person.keys():
    print(f'key: {key}')
# 결과 : key: name
#        key: age
#        key: city

# values() 메서드를 사용한 순회
for value in person.values():
    print(f'Value: {value}')
# 결과 : Value: John
#        Value: 30
#        Value: New York