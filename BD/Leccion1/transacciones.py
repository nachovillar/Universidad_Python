import psycopg2 as bd

conexion = bd.connect(user='postgres',
                      password='Uncharted1',
                      host='127.0.0.1',
                      port='5432',
                      database='test_db'
                      )

try:
    # No se hace el commit de manera automática, por lo que tenemos que indicar el hacer un commit a la base de datos
    # ojo que esta linea no es necesaria, ya que es false por defecto
    # Con el uso de "with" el commit y rollback es automático
    #conexion.autocommit = False

    with conexion:
        with conexion.cursor() as cursor:

            cursor = conexion.cursor()
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Carlos', 'Villar', 'carlosv@mail.com')
            cursor.execute(sentencia, valores)
            #conexion.commit() #acá indicamos el commit

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, mail=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Peralta', 'juanp@mail.com', 1)
            cursor.execute(sentencia, valores)
            #conexion.commit()  # acá indicamos el commit

except Exception as e:
    conexion.rollback()
    print(f'Ocurrió un error, se ha hecho rollback: {e}')

finally:
    conexion.close()
    print(f'Termina la transacción, se hizo commit')