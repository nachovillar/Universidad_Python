class Computadora:
    contadorComputadoras = 0

    @classmethod
    def aumentarContadorComputadora(cls):
        cls.contadorComputadoras += 1

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.aumentarContadorComputadora()
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'COMPUTADORA'.center(100, '+') + f'\nID Computadora: {self.idComputadora} | Nombre: {self.nombre} \n{self.monitor.__str__()} \n{self.teclado.__str__()} \n{self.raton.__str__()}'

    @property
    def idComputadora(self):
        return self._idComputadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

