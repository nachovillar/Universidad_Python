import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p', #Formato de la Hora %I, es en Minutos %M, Segundos %S y el horario %p AM o PM
                handlers = [
                    log.FileHandler('capa_datos.log'), #Vamos a enviar información a un archivo capa_datos.log
                    log.StreamHandler() #También le vamos a enviar la info a la consola
                    ]

                )

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')