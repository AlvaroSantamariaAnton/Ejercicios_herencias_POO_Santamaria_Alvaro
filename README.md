# Descripción de los Scripts

## Ejercicio a - Herencia simple

Este script implementa dos clases `Punto2D` y `Punto3D` para representar puntos en un plano bidimensional y tridimensional respectivamente. La clase `Punto3D` hereda de `Punto2D`, demostrando así un ejemplo básico de herencia en Python.

### Clase `Punto2D`
- **Métodos:**
  - `__init__(self, x, y)`: Constructor que inicializa las coordenadas `x` e `y`.
  - `traslacion(self, dx, dy)`: Método para trasladar el punto en el plano.
  - `__str__(self)`: Método para representar el punto como una cadena de texto.

### Clase `Punto3D`
- **Métodos:**
  - `__init__(self, x, y, z)`: Constructor que inicializa las coordenadas `x`, `y` y `z`.
  - `traslacion(self, dx, dy, dz)`: Método para trasladar el punto en el espacio tridimensional.
  - `__str__(self)`: Método para representar el punto como una cadena de texto.

## Ejercicio b - Puzzle

Este script contiene dos clases `Base` y `Derivada` para demostrar la sobrescritura de métodos y el uso de `super()` en Python.

### Clase `Base`
- **Métodos:**
  - `__init__(self)`: Constructor que inicializa atributos `a`, `b` y `c`.
  - `A(self)`: Método para imprimir el valor de `a`.
  - `B(self)`: Método para imprimir el valor de `b`.
  - `C(self)`: Método para imprimir el valor de `c`.

### Clase `Derivada`
- **Métodos:**
  - `__init__(self)`: Constructor que sobrescribe `a` y llama al constructor de la clase base.
  - `A(self)`: Método para imprimir el valor de `a`.
  - `B(self)`: Método para sobrescribir `b` y luego llamar al método de la clase base.
  - `C(self)`: Método para sobrescribir `c`.

## Ejercicio c - Herencia múltiple

Este script implementa cuatro clases `A`, `B`, `C` y `D` para demostrar la herencia múltiple en Python.

### Clase `A`
- **Métodos:**
  - `__init__(self, a, b, c)`: Constructor que inicializa atributos `a`, `b` y `c`.

### Clase `B`
- **Métodos:**
  - `__init__(self, a, b, c)`: Constructor que llama al constructor de la clase base `A`.

### Clase `C`
- **Métodos:**
  - `__init__(self, a, b, c)`: Constructor que llama al constructor de la clase base `A`.

### Clase `D`
- **Métodos:**
  - `__init__(self, a, b, c, d=None)`: Constructor que llama al constructor de una de las clases bases `B` o `C` (según el MRO) y añade el atributo `d`.

## Ejercicio d - Herencia Caso Real

Este script simula un caso real de herencia y composición en el contexto de una casa con paredes y ventanas.

### Clase `Pared`
- **Métodos:**
  - `__init__(self, orientacion)`: Constructor que inicializa una pared con orientación y una lista de ventanas.
  - `agregar_ventana(self, ventana)`: Método para agregar una ventana a la lista de ventanas.
  - `calcular_superficie_acristalada(self)`: Método para calcular la superficie total acristalada de la pared.

### Clase `ParedCortina`
- **Métodos:**
  - `__init__(self, orientacion, superficie_cortina)`: Constructor que inicializa una pared cortina con orientación y superficie total.
  - `calcular_superficie_acristalada(self)`: Método para devolver la superficie acristalada total de la pared cortina.

### Clase `Ventana`
- **Métodos:**
  - `__init__(self, pared, superficie, proteccion)`: Constructor que inicializa una ventana y la agrega a una pared.
  
### Clase `Casa`
- **Métodos:**
  - `__init__(self, paredes)`: Constructor que inicializa una casa con una lista de paredes.
  - `calcular_superficie_acristalada_total(self)`: Método para calcular la superficie acristalada total de la casa.

## Ejecución

Cada script contiene un bloque condicional `if __name__ == "__main__":` para ejecutar ejemplos de uso de las clases definidas y mostrar sus funcionalidades. Para ejecutar un script, simplemente ejecuta el archivo Python correspondiente.

# Link al repositorio
https://github.com/AlvaroSantamariaAnton/Ejercicios_herencias_POO_Santamaria_Alvaro.git