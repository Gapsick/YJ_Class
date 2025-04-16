import numpy as np

num_features = 3
num_samples = 2

np.random.seed(1)
np.set_printoptions(suppress=True, precision=3)
X = np.random.rand(num_samples, num_features)
# h(x) = wx1 + wx2 + wx3 + b
w_true = np.random.randint(1, 10, num_features)
b_true = np.random.randn() * 0.5

y = X @ w_true + b_true

w = np.random.rand(num_features)
b = np.random.randn()
learning_rate = 0.01
epochs = 100

gradient = np.zeros(num_features)

# prediction
prediction = X @ w + b

# error
error = prediction - y

# gradient
gradient = X.T @ error / num_samples

w = w - learning_rate * gradient
b = b - learning_rate * error.mean()

print(w)
