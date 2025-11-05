from sistems import *

# Ejercicio de Sistemas 3

print("========= Ejercicio de Sistemas 3 =========")

square = Cuadrado("Rojo", 4)
triangle = Triangulo("Azul", 3, 4, [3, 4, 5])
circle = Circulo("Verde", 5)

print(f"Cuadrado - Área: {square.calcular_area()}, Perímetro: {square.calcular_perimetro()}")
print(f"Triángulo - Área: {triangle.calcular_area()}, Perímetro: {triangle.calcular_perimetro()}")
print(f"Círculo - Área: {circle.calcular_area()}, Perímetro: {circle.calcular_perimetro()}")

print()