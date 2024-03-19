"""
Ejercicio b - Puzzle

Explicación:
------------
- base.A() muestra "a" ya que Base tiene un atributo a inicializado como "a".
- derivada.A() muestra "aa" porque el constructor de Derivada sobrescribe el atributo a con "aa".
- base.B() muestra "b" porque Base tiene un atributo b inicializado como "b".
- derivada.B() muestra "b" después de llamar al método super().B(), que imprime "b" (valor de Base.b) y luego sobrescribe el valor de derivada.b con "bb".
- base.C() muestra "c" ya que Base tiene un atributo c inicializado como "c".
- derivada.C() muestra "cc" después de que el constructor de Derivada sobrescribe el atributo c con "cc".
- derivada = base hace que la variable derivada apunte a la misma instancia que base.
- derivada.C() muestra "c" porque ahora derivada apunta a la instancia de Base, y el valor de c no ha cambiado en esa instancia.
"""

class Base: 
    def __init__(self): 
        self.a = "a"  # Inicializa el atributo 'a' con el valor "a"
        self.b = "b"  # Inicializa el atributo 'b' con el valor "b"
        self.c = "c"  # Inicializa el atributo 'c' con el valor "c"

    def A(self): 
        print(self.a)  # Muestra el valor de 'a'

    def B(self): 
        print(self.b)  # Muestra el valor de 'b'

    def C(self): 
        print(self.c)  # Muestra el valor de 'c'

class Derivada(Base): 
    def __init__(self): 
        self.a = "aa"  # Sobrescribe el valor de 'a' con "aa"
        super().__init__()  # Llama al constructor de la clase base para inicializar 'b' y 'c'
        self.c = "cc"  # Sobrescribe el valor de 'c' con "cc"

    def A(self): 
        print(self.a)  # Muestra el valor de 'a'

    def B(self): 
        self.b = "bb"  # Sobrescribe el valor de 'b' con "bb"
        super().B()  # Llama al método 'B' de la clase base
        print(self.b)  # Muestra el valor de 'b'


if __name__ == "__main__":
    # Creación de instancias de las clases Base y Derivada
    base = Base()  # Crea una instancia de la clase Base
    derivada = Derivada()  # Crea una instancia de la clase Derivada

    # Llamadas a los métodos de las instancias
    base.A()  # Muestra "a"
    derivada.A()  # Muestra "aa"

    print()  # Imprime una línea en blanco

    base.B()  # Muestra "b"
    derivada.B()  # Muestra "b" y luego "bb"

    base.C()  # Muestra "c"
    derivada.C()  # Muestra "cc"

    # Asigna la instancia de base a derivada
    derivada = base

    # Muestra "c" ya que derivada ahora apunta a la instancia de Base
    derivada.C()  # Muestra "c"
