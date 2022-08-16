from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0

    @classmethod
    def aumentarContadorRatones(cls):
        cls.contadorRatones += 1

    def __init__(self, tipoEntrada, marca):
        Raton.aumentarContadorRatones()
        super().__init__(tipoEntrada, marca)
        self._idRaton = Raton.contadorRatones

    def __str__(self):
        return f'RATÓN'.center(50, '*') + f'\nID Raton: {self.idRaton}   {super().__str__()}'

    @property
    def idRaton(self):
        return self._idRaton

if __name__ == '__main__':
    raton = Raton('USB', 'Logitech')
    print(raton)