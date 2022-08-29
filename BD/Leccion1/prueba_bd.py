import psycopg2

conexion = psycopg2.connect(user='postgres',
                            password='Uncharted1',
                            host='127.0.0.1',
                            port='5432',
                            database='test_db'
                            )
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * ' \
                        'FROM persona ' \
                        'WHERE id_persona = %s'
            id_persona = input('Proporcione el ID de la persona que busca: ')
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrió un error: {e}')

finally:
    conexion.close()
