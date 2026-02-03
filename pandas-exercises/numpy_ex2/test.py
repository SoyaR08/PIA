import numpy as np

# 8. Autovalores y Autovectores

A = np.array([[2, 1], [1, 3]])

print(np.linalg.eigvals(A))
print(np.linalg.eig(A))