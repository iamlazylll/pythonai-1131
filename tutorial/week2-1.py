import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

x_mean = np.mean(X)
y_mean = np.mean(y)

m = np.sum((X - x_mean) * (y - y_mean) / np.sum((X - x_mean) ** 2))

b = y_mean - m * x_mean

print(f"斜率 (m): {m}")
print(f"截距 (b): {b}")

def predict(x):
  return m * x + b

predictions = predict(X)
print(f"預測結果: {predictions}")
