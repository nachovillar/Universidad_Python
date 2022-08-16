class Monitor:
    contadorMonitores = 0

    @classmethod
    def aumentarContadorMonitores(cls):
        cls.contadorMonitores += 1

    def __init__(self, marca, tamaño):
        Monitor.aumentarContadorMonitores()
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'MONITOR'.center(50, '*') + f'\nID Monitor: {self.idMonitor} | Marca: {self.marca} | Tamaño: {self.tamaño}'

    @property
    def idMonitor(self):
        return self._idMonitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

