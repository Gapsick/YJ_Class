from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

np.set_printoptions(suppress=True)  # 지수 표기 방지

# 1. 데이터셋 로딩 및 분할
digits = load_digits()
X = digits.data     # (1797, 64): 8x8 이미지의 벡터 형태
y = digits.target   # (1797,): 정답 레이블(0~9)

# 2. 학습/테스트 셋 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 3. 입력 데이터 표준화 (평균 0, 표준편차 1)
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 4. 기본 설정
num_features = X_train_std.shape[1]      # 입력 벡터의 차원 (64)
num_samples = X_train_std.shape[0]      # 학습 샘플 수
num_classes = 10                        # 분류할 클래스 개수 (0~9)

# 5. 원-핫 인코딩
one_hot = np.eye(num_classes)           # (10, 10) 단위행렬
y_train_one_hot = one_hot[y_train]      # (학습 샘플 수, 10) = (1437, 10)
y_test_one_hot = one_hot[y_test]       # (테스트 샘플 수, 10)

# 6. 하이퍼파라미터 및 가중치 초기화
learning_rate = 0.01
epochs = 1  # 실습용 1회 학습 (실제 학습 시 증가 필요)
W = np.random.randn(num_features, num_classes)  # (64, 10): 가중치
b = np.zeros(num_classes)                       # (10, ): 바이어스

# 7. 학습 루프
for epoch in range(epochs):
    logits = X_train_std @ W + b                        # (N. K): 선형 결합 결과
    logits -= np.max(logits, axis=1, keepdims=True)     # softmax 안정화 trick

    exp_logits = np.exp(logits)                         # (N, K): 지수 함수 적용
    sum_exp = np.sum(exp_logits, axis=1, keepdims=True) # (N, 1): 클래스별 합
    softmax_probs = exp_logits / sum_exp                # (N, K): 소프트맥스 확률

    error = softmax_probs - y_train_one_hot             # (N, K): 오차 (예측 - 정답)

    # 가중치 및 바이어스 기울기 계산
    grab_W = X_train_std.T @ error / num_samples        # (94, 10)
    grab_b = error.mean(axis=0)                         #  (10,)

    # 경사하강법을 이용한 파라미터 업데이트
    W -= learning_rate * grab_W
    b -= learning_rate * grab_b

    # 크로스 엔트로피 손실 계산
    loss = -np.sum(y_train_one_hot * np.log(softmax_probs + 1e-15)) / num_samples

    if epoch % 1000 == 0:
        print(f"Train Loss : {loss:.4f}")

# 8. 테스트셋 예측 및 평가
test_logits = X_test_std @ W + b
test_logits -= np.max(test_logits, axis=1, keepdims=True)
test_exp_logits = np.exp(test_logits)
test_sum_exp = np.sum(test_exp_logits, axis=1, keepdims=True)
test_softmax_probs = test_exp_logits / test_sum_exp

# 테스트 손실 계산
test_loss = -np.sum(y_test_one_hot * np.log(test_softmax_probs + 1e-15)) / X_test.shape[0]

# 예측값: 확률이 가장 높은 클래스 선택
y_pred = np.argmax(test_softmax_probs, axis=1)

# 정확도 계산
accuracy = (y_pred == y_test).mean()

print(f"Test Loss: {test_loss:.4f}")
print(f"Accuracy: {accuracy:.4f}")