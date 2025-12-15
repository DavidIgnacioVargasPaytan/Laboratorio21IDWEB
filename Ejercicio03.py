import math

class FiguraGeometrica:
    def __init__(self, nombre):
        """Constructor de la clase base."""
        self.nombre = nombre

    def calcular_area(self):
        """Método abstracto para calcular el área."""
        raise NotImplementedError("Este método debe ser sobrescrito por las clases hijas.")

    def calcular_perimetro(self):
        """Método abstracto para calcular el perímetro."""
        raise NotImplementedError("Este método debe ser sobrescrito por las clases hijas.")

    def mostrar_datos(self):
        """Muestra los datos de la figura."""
        print(f"\n--- {self.nombre} ---")
        try:
            print(f"Área: {self.calcular_area():.2f}")
            print(f"Perímetro: {self.calcular_perimetro():.2f}")
        except NotImplementedError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error al calcular: {e}")

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3, altura=None):
        super().__init__("Triángulo")
        self.lados = (lado1, lado2, lado3)
        self.altura = altura
        self.base = lado1 

    def calcular_perimetro(self):
        return sum(self.lados)

    def calcular_area(self):
        s = self.calcular_perimetro() / 2
        return math.sqrt(s * (s - self.lados[0]) * (s - self.lados[1]) * (s - self.lados[2]))

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

rectangulo = Rectangulo(base=10, altura=5)
triangulo = Triangulo(lado1=3, lado2=4, lado3=5)
circulo = Circulo(radio=7)

lista_figuras = [rectangulo, triangulo, circulo]

for figura in lista_figuras:
    figura.mostrar_datos()