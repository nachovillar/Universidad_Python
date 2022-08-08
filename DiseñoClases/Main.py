from Producto import Producto
from Orden import Orden

if __name__ == '__main__':
    salsa = Producto('Salsa', 650)
    arroz = Producto('Arroz', 2000)
    porotos = Producto('Porotos', 1800)
    ajo = Producto('Ajo', 200)

    Compra_Jose = Orden([salsa, arroz])
    Compra_Jose.agregar_producto(porotos)
    print(Compra_Jose)

    compra_josh = Orden([porotos, ajo])
    print(compra_josh)

