import numpy as np

num_of_samples = 5
num_of_features = 2

# data set
np.random.seed(1)
np.set_printoptions(False, suppress=True)   # 지수 X
X = np.random.rand(num_of_samples, num_of_features) * 10    #스칼라 연산
x_true = [5, 3]
b_true = 4
noise = np.random.randn(num_of_samples) * 0.5
y = X[:, 0] * 5 + X[:, 1] * 3 + b_true + noise


print(X)
print(y)
