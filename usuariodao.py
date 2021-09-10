from cursor_del_pool import CursorDelPool
from conexion import Conexion
from usuario import Usuario
from logger_base import log

class UsuarioDAO:
    _seleccionar = 'SELECT * FROM usuario ORDER BY id_usuario'
    _insertar = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _actualizar = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _eliminar = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._seleccionar)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._insertar, valores)
            log.debug(f'Usuario insertado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._actualizar, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            log.debug(f'Objeto eliminado: {usuario}')
            valores = (usuario.id_usuario,)
            cursor.execute(cls._eliminar, valores)
            return cursor.rowcount