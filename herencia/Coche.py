from Vehiculo import *

class Coche(Vehiculo):
    def __init__(self, color: str, ruedas: int, velocidad: int):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return f'Coche'.center(50, '-') + '\n' + f'{super().__str__()} Velocidad: {self._velocidad}'

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

if __name__ == '__main__':
    coche1 = Coche('verde', 2, 150)
    print(coche1)

