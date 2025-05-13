import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. 데이터 로드 및 분할
dataset = load_breast_cancer()
X = dataset.data
y = dataset.target

# 2. 훈련/테스트 셋 분리 (클래스 비율 유지)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, stratify=y, test_size=0.2, random_state=42    # stratify=y -> true와 false값을 동일한 비율
)

# 3. 특성 표준화 (평균 0, 분산 1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

num_features = X_train.shape[1] # 30

w = np.random.randn(num_features, 1)
b = np.random.randn()
learning_rate = 0.01
np.set_printoptions(suppress=True, precision=5)

y_train = y_train.reshape(-1, 1)    # collum을 1개로 만들기 -> 1차원을 2차원으로 변경
# z = wx + b
z = X_train @ w + b

# prediction = 1 / (1 + e^(-z))
prediction = 1 / (1 + np.exp(-z))

# error = prediction - y_train  (455, 1) - (455, 1)
error = prediction - y_train

# gradient_w, gradient_b
gradient_w = X_train.T @ error/ len(X_train)
gradient_b = error.mean()

# update parameters : w, b
w = w - learning_rate * gradient_w
b = b - learning_rate * gradient_b

# calculate loss
loss = -np.mean(y_train*np.log(prediction) + (1 - y)*np.log(1 - prediction))