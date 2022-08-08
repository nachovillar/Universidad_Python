class Color():

    def __init__(self, color):
        try:
            if self._validation_Color(color):
                self._color = color
        except:
            print(f'El argumento Color no es una cadena de caracteres')

    def __str__(self):
        return f'Color: {self._color}'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    def _validation_Color(self, color):
        return True if isinstance(color, str) else False