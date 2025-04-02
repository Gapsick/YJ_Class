from sklearn.model_selection import train_test_split
import numpy as np

# X : 입력 값
X = np.random.rand(10, 2) * 5
# y : 출력 값 (정답)
y = np.random.randint(0, 2, size=10)

X_train, X_test, y_train, y_text = \
    train_test_split(X, y, test_size=0.2, random_state=1)

print(f"X_train.shape: {X_train.shape}")
print(X_train)