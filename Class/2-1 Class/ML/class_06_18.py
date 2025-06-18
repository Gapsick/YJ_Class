from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# 1. 데이터셋 로딩 및 분할
digits = load_digits()
features = digits.data                    # (1797, 64): 8x8 이미지 벡터
labels = digits.target                    # (1797,): 0~9 클래스 정수

# 2. 학습/테스트 셋 분할
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42, stratify=labels # 동일한 비율로 나누기
)

# 3. 표준화 (평균 0, 분산 1)
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

np.set_printoptions(suppress=True)
num_features = X_train_std.shape[1] # 64
num_samples = X_train_std.shape[0] # 1437
num_classes = 10

W = np.random.randn(num_features, num_classes)   # 64, 10 
b = np.zeros(num_classes)   # (10,)
learning_rate = 0.01
epochs = 10000

for epoch in range(epochs):
    # X (1437, 64) @ W(64, 10) + b      # 64: Pixel, 1437장 있는거, 10은 class -> class 별로 다 더하기
    logit = X_train_std @ W + b    # (1437, 10) -> 각 class 별로 만들기
    logit_max = np.max(logit, axis=1, keepdims=True)    # 1437 vector 구조(1차원)로 나오는거 방지
    logit -= logit_max  # 값이 발산하는걸 방지 -> 최대값은 0 (자기자신), 다른값(음수)이 높아지면 0으로 수렴 함
    exp_logit = np.exp(logit)   # 1437, 10
    exp_logit_sum = np.sum(exp_logit, axis=1, keepdims=True)   # 각 Class별 합 -> 1437, 1   
    softmax = exp_logit / exp_logit_sum

    i_matrix = (np.eye(num_classes))
    one_hot = i_matrix[y_train] # 1437, 10

    # error = softmax(1437, 10) - one_hot (1437, 10)

    error = softmax - one_hot   # 예측값 (확률값 그 자체) - 정답

    gradient_w = X_train_std.T @ error / num_samples
    gradient_b = np.sum(error, axis=0) / num_samples

    # update
    W -= learning_rate * gradient_w
    b -= learning_rate * gradient_b

    # loss
    loss = -np.sum(np.log(softmax + 1e-15) * one_hot) / num_samples # 1e-15 -> 언더플로우 방지

    if epoch % 1000 == 0:
        print(loss)


def predict(arg_X, arg_label):
    logit = X_train_std @ W + b # 10
    logit_max = np.max(logit, keepdims=True)    # 1437 vector 구조(1차원)로 나오는거 방지
    logit -= logit_max  # 값이 발산하는걸 방지 -> 최대값은 0 (자기자신), 다른값(음수)이 높아지면 0으로 수렴 함
    exp_logit = np.exp(logit)   # 1437, 10
    exp_logit_sum = np.sum(exp_logit, axis=1, keepdims=True)   # 각 Class별 합 -> 1   
    softmax = exp_logit / exp_logit_sum

    predict = np.argmax(softmax)

    print(f"label: {arg_label}, predict: {predict}")

for idx in range(0, 10):
    predict(X_test_std[idx], y_test[idx])