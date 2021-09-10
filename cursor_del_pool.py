from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipoExcepcion, valorExcepcion, detalleExcepcion):
        log.debug('Se ejecuta método __exit__')
        if valorExcepcion:
            self._conexion.rollback()
            log.error(f'Ocurrió una excepción: {valorExcepcion} {tipoExcepcion} {detalleExcepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)
        