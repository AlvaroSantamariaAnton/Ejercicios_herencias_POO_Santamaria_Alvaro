"""
Ejercicio c - Herencia múltiple
"""

# Definición de la clase A
class A:
    def __init__(self, a, b, c):
        self.a = a  # Inicialización del atributo 'a'
        self.b = b  # Inicialización del atributo 'b'
        self.c = c  # Inicialización del atributo 'c'


# Definición de la clase B que hereda de A
class B(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)  # Llama al constructor de la clase base A con los mismos argumentos


# Definición de la clase C que hereda de A
class C(A):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)  # Llama al constructor de la clase base A con los mismos argumentos


# Definición de la clase D que hereda de B y C
class D(B, C):
    def __init__(self, a, b, c, d=None):  # Modificación para aceptar un argumento opcional 'd'
        super().__init__(a, b, c)  # Llama al constructor de la clase base B o C (según el orden de resolución MRO)
        self.d = d  # Inicialización del atributo 'd'


if __name__ == "__main__":
    # Pruebas
    d = D(1, 2, 3)  # Creación de una instancia de la clase D sin proporcionar 'd'
    print(isinstance(d, A), isinstance(d, B), isinstance(d, C))  # Comprobación de instancias: True True True 
    print(d.a, d.b, d.c)  # Impresión de los atributos 'a', 'b', y 'c': 1 2 3