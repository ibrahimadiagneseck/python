import numpy as np

a, b = 2, 5
a, b = b, a
print(a, b)

A = np.array([[1, 2, 3],[4, 5, 6]])

tmp = np.copy(A[0, :])
A[0, :] = A[1, :]
A[1, :] = tmp
print(A)

