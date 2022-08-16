from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas as cp

if __name__ == '__main__':
    while(1):
        try:
            print(f'Opciones: \n'
                  f'1. Agregar Película\n'
                  f'2. Listar Películas\n'
                  f'3. Eliminar Catálogo de Películas\n'
                  f'4. Salir\n')
            opcion = int(input('Elija una opción: '))
        except Exception as e:
            print('Ocurrió un Error {e}')
            opcion = None

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)

        elif opcion == 2:
            cp.listar_peliculas()

        elif opcion == 3:
            cp.eliminar()

        elif opcion == 4:
            print(f'Saliendo del programa...')
            break

        else:
            print(f'El número ingresado no está dentro de las opciones, por favor ingrese una opción correcta')



