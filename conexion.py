from logger_base import log
from psycopg2 import pool
import sys

class Conexion:

    _database = "test_db"
    _username = "postgres"
    _password = "admin"
    _port = "5432"
    _host = "127.0.0.1"
    _min_con = 1
    _max_con = 3
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._min_con,
                    cls._max_con,
                    host = cls._host,
                    user = cls._username,
                    password = cls._password,
                    port = cls._port,
                    database = cls._database
                )
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool {e}')
                sys.exit
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión del pool obtenida: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall