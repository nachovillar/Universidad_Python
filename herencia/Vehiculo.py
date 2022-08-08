class Vehiculo():
    def __init__(self, color: str, ruedas: int):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f' Color : {self._color}  Ruedas: + {self._ruedas}'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

