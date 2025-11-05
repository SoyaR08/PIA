import math

class Figura:
    def __init__(self, color, shape_type):
        self.color = color
        self.shape_type = shape_type


class Circulo(Figura):
    def __init__(self, color, radius):
        super().__init__(color, "Círculo")
        self.radius = radius

    def calcular_area(self):
        return math.pi * self.radius ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radius


class Triangulo(Figura):
    def __init__(self, color, base, height, sides):
        super().__init__(color, "Triángulo")
        self.base = base
        self.height = height
        self.sides = sides if isinstance(sides, list) and len(sides) == 3 else [base, height, math.hypot(base, height)]

    def calcular_area(self):
        return (self.base * self.height) / 2

    def calcular_perimetro(self):
        return sum(self.sides)


class Cuadrado(Figura):
    def __init__(self, color, side_length):
        super().__init__(color, "Cuadrado")
        self.side_length = side_length

    def calcular_area(self):
        return self.side_length ** 2

    def calcular_perimetro(self):
        return 4 * self.side_length
