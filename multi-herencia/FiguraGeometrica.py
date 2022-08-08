from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    def __init__(self, alto: float, ancho: float):
        try:
            if self._validation_number(alto):
                self._alto = alto

        except ValueError:
            print(f'El argumento alto no es un número')

        try:
            if self._validation_number(ancho):
                self._ancho = ancho
        except ValueError:
            print(f'El argumento ancho no es un número')

    def __str__(self):
        return f'Alto: {self._alto} | Ancho: {self._ancho}'

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto: float):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho: float):
        self._ancho = ancho

    def _validation_number(self, number):
        return True if isinstance(number, int) or isinstance(number, float) else False

    @abstractmethod
    def area(self):
        pass
            
if __name__ == '__main__':
    figura = FiguraGeometrica(3.21, 2.22)
    figura.ancho = 2
    print(figura)