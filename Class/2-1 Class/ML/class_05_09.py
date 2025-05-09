from sklearn.datasets import load_breast_cancer
import matplotlib.pyplot as plt

cancer = load_breast_cancer()

print(cancer.data.shape, cancer.target.shape)

print(cancer.feature_names)

print(cancer.data[0:3])

plt.scatter(cancer.data[:, 0], cancer.target)
plt.show()

print(cancer.data.shape, cancer.target.shape)

print(cancer.feature_names)

print(cancer.target[:100])

plt.scatter(cancer.data[: 0], cancer.target)

plt.show()