from Vehiculo import *

class Bicicleta(Vehiculo):

    def __init__(self, color: str, ruedas: int, tipo: str):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return f'Bicicleta'.center(50, '-') + '\n' + f'{super().__str__()} Tipo: {self._tipo}'

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

if __name__ == '__main__':
    bicicleta1 = Bicicleta('amarilla', 1, 'Mono')
    print(bicicleta1)