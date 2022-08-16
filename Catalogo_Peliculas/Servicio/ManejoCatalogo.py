class ManejoCatalogo:
    def __init__(self, nombreArchivo):
        self._nombreArchivo = nombreArchivo

    def __enter__(self, nombreArchivo):
        self._nombreArchivo = open(self._nombreArchivo, 'r+', encoding='utf8')
        return self._nombreArchivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._nombreArchivo:
            self._nombreArchivo.close()