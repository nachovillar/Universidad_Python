class Orden:
    contadorOrden = 0

    @classmethod
    def aumentarContadorOrden(cls):
        cls.contadorOrden += 1

    def __init__(self, computadoras):
        Orden.aumentarContadorOrden()
        self._idOrden = Orden.contadorOrden
        self._computadoras = list(computadoras)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += computadora.__str__() + '\n'
        return computadoras_str

    @property
    def idOrden(self):
        return self._idOrden

    @property
    def computadoras(self):
        return self._computadoras

    def agregarComputadora(self, computadora):
        self.computadoras.append(computadora)
