import os

class CatalogoPeliculas:
    rutaArchivo = 'C:\\Users\\jose-\\Desktop\\Curso Python\\Universidad_Python\\Catalogo_Peliculas\\Peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.rutaArchivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        try:
            if os.stat(CatalogoPeliculas.rutaArchivo).st_size == 0:
                print(f'El Catálogo está vacío'.center(50, '*'))
            else:
                with open(cls.rutaArchivo, 'r', encoding='utf8') as archivo:
                    print('Catalogo de Peliculas'.center(50, '*'))
                    print(archivo.read())
        except Exception as e:
            print(f'Ocurrió un error: {e}')

    @classmethod
    def eliminar(cls):
        try:
            os.remove(cls.rutaArchivo)
            print(f'Archivo eliminado'.center(50, '*'))

        except IOError as e:
            print(f'Ha ocurrido un error: {e}')
