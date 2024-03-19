"""
Ejercicio a - Herencia simple
"""
# Definición de la clase Punto2D
class Punto2D:
    # Constructor que inicializa los atributos x e y
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # Método para trasladar el punto
    def traslacion(self, dx, dy):
        self.x += dx
        self.y += dy
        
    # Método para representar el punto como una cadena
    def __str__(self):
        return f"X: {self.x}; Y: {self.y}"


if __name__ == "__main__":
    # Ejemplo de uso de la clase Punto2D
    a = Punto2D(1, 2)  # Creación de un punto 2D en las coordenadas (1, 2)
    print("A = {}".format(a))  # Imprime las coordenadas del punto creado

    # Traslada el punto a nuevas coordenadas (-1, -2)
    a.traslacion(-1, -2)
    print("A = {}".format(a))  # Imprime las nuevas coordenadas del punto tras la traslación

    # Creación de otro punto 2D en las coordenadas (-3, 0)
    b = Punto2D(-3, 0)
    print("B = {}".format(b))  # Imprime las coordenadas del nuevo punto creado

    # Traslada el punto b a nuevas coordenadas (5, -1)
    b.traslacion(5, -1)
    print("B = {}".format(b))  # Imprime las nuevas coordenadas del punto b tras la traslación


# Definición de la clase Punto3D, que hereda de Punto2D
class Punto3D(Punto2D):
    # Constructor que inicializa los atributos x, y, z
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Llama al constructor de la clase base (Punto2D)
        self.z = z
        
    # Método para trasladar el punto en el espacio tridimensional
    def traslacion(self, dx, dy, dz):
        super().traslacion(dx, dy)  # Llama al método traslacion de la clase base (Punto2D)
        self.z += dz
        
    # Método para representar el punto como una cadena
    def __str__(self):
        return f"X: {self.x}; Y: {self.y}; Z: {self.z}"


if __name__ == "__main__":
    # Ejemplo de uso de la clase Punto3D
    c = Punto3D(1, 5, -3)  # Creación de un punto 3D en las coordenadas (1, 5, -3)
    print("C = {}".format(c))  # Imprime las coordenadas del punto creado

    # Traslada el punto c a nuevas coordenadas (0, -2, 1)
    c.traslacion(0, -2, 1)
    print("C = {}".format(c))  # Imprime las nuevas coordenadas del punto c tras la traslación
