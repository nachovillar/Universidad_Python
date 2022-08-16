from Orden import Orden
from Computadora import Computadora
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton

if __name__ == '__main__':
    monitor =  Monitor('Samsung', '27')
    teclado = Teclado('USB', 'Red Dragon')
    raton = Raton('USB', 'Logitech')
    computadora = Computadora('ASUS', monitor, teclado, raton)
    orden = Orden([computadora])

    monitor2 =  Monitor('Samsung', '27')
    teclado2 = Teclado('USB', 'Red Dragon')
    raton2 = Raton('USB', 'Logitech')
    computadora2 = Computadora('ASUS', monitor2, teclado2, raton2)

    orden.agregarComputadora(computadora2)

    print(orden)