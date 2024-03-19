"""
Ejercicio d - Herencia Caso Real
"""

class Pared:
    # Representa una pared con una orientación específica y una lista de ventanas.

    def __init__(self, orientacion):
        # Inicializa una nueva pared con la orientación especificada y una lista vacía de ventanas.

        self.orientacion = orientacion
        self.ventanas = []

    def agregar_ventana(self, ventana):
        # Agrega una ventana a la lista de ventanas de la pared.

        self.ventanas.append(ventana)

    def calcular_superficie_acristalada(self):
        # Calcula la superficie total acristalada de la pared sumando las superficies de todas sus ventanas.

        return sum(ventana.superficie for ventana in self.ventanas)


class ParedCortina(Pared):
    # Representa una pared cortina que hereda de la clase Pared.

    def __init__(self, orientacion, superficie_cortina):
        # Inicializa una pared cortina con la orientación y superficie total especificadas.
        
        super().__init__(orientacion)
        self.superficie_cortina = superficie_cortina

    def calcular_superficie_acristalada(self):
        # Devuelve la superficie acristalada total de la pared cortina.

        return self.superficie_cortina


class Ventana:
    # Representa una ventana en una pared con una superficie y protección específicas.

    def __init__(self, pared, superficie, proteccion):
        # Inicializa una nueva ventana y la agrega a la pared especificada.

        if proteccion is None:
            raise Exception("Se requiere una protección para la ventana.")
        self.pared = pared
        self.superficie = superficie
        self.proteccion = proteccion
        pared.agregar_ventana(self)


class Casa:
    # Representa una casa con una lista de paredes.

    def __init__(self, paredes):
        # Inicializa una nueva casa con la lista de paredes especificada.

        self.paredes = paredes

    def calcular_superficie_acristalada_total(self):
        # Calcula y devuelve la superficie acristalada total de la casa sumando las superficies acristaladas de todas sus paredes.

        return sum(pared.calcular_superficie_acristalada() for pared in self.paredes)


def main():
    # Instanciación de las paredes
    pared_norte = Pared("NORTE")
    pared_oeste = Pared("OESTE")
    pared_sur = Pared("SUR")
    pared_este = Pared("ESTE")

    # Instanciación de las ventanas con protección
    ventana_norte = Ventana(pared_norte, 0.5, "Persiana")  # Para comprobar que se cumple la excepción, sustituir el valor de protección por "None"
    ventana_oeste = Ventana(pared_oeste, 1, "Persiana")
    ventana_sur = Ventana(pared_sur, 2, "Estor")
    ventana_este = Ventana(pared_este, 1, "Estor")

    # Instanciación de la casa con las 4 paredes
    casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])
    print("Superficie acristalada inicial:", casa.calcular_superficie_acristalada_total())

    # Reemplazo de una pared por una pared cortina
    casa.paredes[2] = ParedCortina("SUR", 10)
    print("Superficie acristalada final:", casa.calcular_superficie_acristalada_total())


if __name__ == "__main__":
    main()