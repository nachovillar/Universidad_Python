class Producto:
    contador_productos = 0

    @classmethod
    def aumentar_contador_producto(cls):
        cls.contador_productos += 1

    def __init__(self, nombre, precio):
        Producto.aumentar_contador_producto()
        self._id_producto = Producto.contador_productos
        self._nombre = nombre if self._validation_name(nombre) else print('El nombre es inválido')
        self._precio = precio if self._validation_price(precio) else print('El precio es inválido')

    def __str__(self):
        return f'[ID Producto: {self.id_producto} | Nombre: {self.nombre} | Precio: {self.precio}] \n'

    @property
    def id_producto(self):
        return self._id_producto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def _validation_price(self, number):
        return True if isinstance(number, int) or isinstance(number, float) else False

    def _validation_name(self, name):
        return True if isinstance(name, str) else False

if __name__ == '__main__':
    producto = Producto('p', 111)
    print(producto)
