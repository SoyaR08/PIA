import numpy as np

# 1. Producto Escalar

a = [2, 3, 4]
b = [5, 6, 7]

scalar_product = np.dot(a, b)
print(scalar_product)

# 2. Módulo de un Vector

v = [3, 4]

mod = np.linalg.norm(v)

print(mod)

# 3. Producto de Dos Matrices

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

product = np.dot(A, B)

print(product)

# 4. Matriz Traspuesta

A = np.array([[1, 2, 3], [4, 5, 6]])

print(A.T)

# 5. Traza de una Matriz

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(A.trace())

# 6. Determinante de una Matriz

A = np.array([[1, 2], [3, 4]])

print(np.linalg.det(A))

# 7. Matriz Inversa

A = np.array([[4, 7], [2, 6]])

print(np.linalg.inv(A))

# 8. Autovalores y Autovectores

A = np.array([[2, 1], [1, 3]])

print(np.linalg.eigvals(A))
print(np.linalg.eig(A))

# 9. Solución de un Sistema de Ecuaciones

# 2x + y = 8
# x + 3y = 18

ec1 = np.array([[2, 1], [1, 3]])
ec2 = np.array([8, 18])

solution = np.linalg.solve(ec1, ec2)

print(solution) 