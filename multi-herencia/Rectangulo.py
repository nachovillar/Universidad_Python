from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):

    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def __str__(self):
        return f'Rectangulo'.center(50, '-') + '\n' + f'{FiguraGeometrica.__str__(self)} | {Color.__str__(self)} | Area: {self.area()}'

    def area(self):
        area = self.ancho * self.alto
        return area

if __name__ == '__main__':
    rectangulo = Rectangulo(3, 5, 'Azul')
    print(rectangulo)