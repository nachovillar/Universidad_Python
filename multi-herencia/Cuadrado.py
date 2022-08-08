from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):

    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def __str__(self):
        return f'Cuadrado'.center(50, '-') + '\n' + f'{FiguraGeometrica.__str__(self)} | {Color.__str__(self)} + | Area: {self.area()}'

    def area(self):
        area = self.alto * self.ancho
        return area

if __name__ == '__main__':
    cuadrado = Cuadrado(2, 'verde')
    print(cuadrado)