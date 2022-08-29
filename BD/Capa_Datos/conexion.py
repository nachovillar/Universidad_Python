from logger_base import log
import psycopg2 as bd
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'Uncharted1'
    _DB_PORT = '5432'
    _HOTS = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOTS,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexión exitosa: {cls._conexion}')

                return cls._conexion
            except Exception as e:
                log.error(f'Ocurrió una exepción {e}')
                sys.exit() #termina por completo el programa

        else: #Si ya existe el objeto conexión, lo retornamos ya que ya hay una conexión a la base de datos
            return cls._conexion

    @classmethod
    def obetenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor

            except Exception as e:
                log.error(f'Ocurrió una excepción al obtener el cursos: {e}')
                sys.exit()

        else:
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obetenerCursor()