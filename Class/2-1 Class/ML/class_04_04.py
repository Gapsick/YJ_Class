from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

np.set_printoptions(suppress=True, precision=2)
X = np.random.rand(100, 1) * 10 # 100개의 sample, feature이 1개
y = 2.5 * X + np.random.randn(100, 1) * 2
y = y.ravel()

# 모델 생성(SGD) 후 하이퍼파라메터 설정
model = SGDRegressor(
    max_iter=100,
    learning_rate="constant",
    eta0=0.001,
    penalty=None,
    random_state=0
)

# 학습 실시!!
model.fit(X, y)

# 평가!
# Loss (Cost function) 
y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)
print(f"평균 제곱 오차(MSE): {mse:.4f}")