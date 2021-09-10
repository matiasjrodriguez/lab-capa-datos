from usuariodao import UsuarioDAO
from usuario import Usuario
from logger_base import log

run = True
while run:
    print('1. Listar usuarios.')
    print('2. Agregar usuario.')
    print('3. Modificar usuario.')
    print('4. Eliminar usuario.')
    opcion = int(input('5. Salir\n'))

    if opcion == 1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)

    elif opcion == 2:
        username_var = input('Ingrese username: ')
        password_var = input('Ingrese password: ')
        usuario = Usuario(username = username_var, password = password_var)
        usuarios_insertados = UsuarioDAO.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')

    elif opcion == 3:
        id_usuario_var = int(input('Ingrese ID de usuario: '))
        username_var = input('Ingrese el nuevo username: ')
        password_var = input('Ingrese el nuevo password: ')
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizados = UsuarioDAO.actualizar(usuario)
        log.info(f'Usuarios modificados: {usuarios_actualizados}')

    elif opcion == 4:
        id_usuario_var = int(input('Igngrese ID de usuario: '))
        usuario = Usuario(id_usuario = id_usuario_var)
        usuarios_eliminados = UsuarioDAO.eliminar(usuario)
        log.info(f'Usuarios eliminados: {usuarios_eliminados}')

    elif opcion == 5:
        print('El programa ha finalizado correctamente.')
        run = False
        