from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0

    @classmethod
    def aumentarContadorTeclados(cls):
        cls.contadorTeclados += 1

    def __init__(self, tipoEntrada, marca):
        Teclado.aumentarContadorTeclados()
        super().__init__(tipoEntrada, marca)
        self._idTeclado = Teclado.contadorTeclados

    def __str__(self):
        return f'TECLADO'.center(50, '*') + f'\nID Teclado: {self._idTeclado}  {super().__str__()}'

    @property
    def idTeclado(self):
        return self._idTeclado

if __name__ == '__main__':
    teclado = Teclado('C', 'Red Dragon')
    print(teclado)