class Orden:
    contador_ordenes = 0

    @classmethod
    def aumentar_contador_orden(cls):
        cls.contador_ordenes += 1

    def __init__(self, productos):
        Orden.aumentar_contador_orden()
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def __str__(self):
        productos_str = ''

        for producto in self.productos:
            productos_str += producto.__str__()

        return f'Orden: {self.id_orden} | Total: {self.calcular_total()} \nProductos: \n{productos_str}'

    @property
    def id_orden(self):
        return self._id_orden

    @property
    def productos(self):
        return self._productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total