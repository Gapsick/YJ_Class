from sklearn.datasets import fetch_california_housing

# 1. 데이터 로드
data = fetch_california_housing()

# 2. 주요 속성 확인
X = data.data       # 입력 데이터 (numpy.ndarray)
y = data.target     # 타겟값 (중간 집값, 단위: 100,000$)
feature_message = data.feature_names  # 특성 이름 리스트

print(type(data), type(X), type(feature_message))

print("입력 X shape:", X.shape)
print("입력 y shape:", y.shape)
print("특성 이름:", feature_message)
print("설명:", data.DESCR[:1000])