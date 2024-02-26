def invitados(archivo, modo):
    """
    Función para añadir nombres de invitados a un archivo.

    :param archivo: Nombre del archivo donde se guardarán los nombres de los invitados.
    :param modo: Modo de apertura del archivo ('w', 'x' o 'a').
    :return: None
    >>> invitados('invitados.txt', 'w')
    ¡Bienvenido al libro de invitados!
    Por favor, ingresa tu nombre: Alice
    Hola, Alice! Gracias por tu visita.
    >>> invitados('invitados.txt', 'x')  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    FileExistsError:
    >>> invitados('invitados.txt', 'a')
    ¡Bienvenido al libro de invitados!
    Por favor, ingresa tu nombre: Bob
    Hola, Bob! Gracias por tu visita.
    >>> import os
    >>> os.remove('invitados.txt')  # Limpiar el archivo después de las pruebas
    """
    # Mensaje de bienvenida
    print("¡Bienvenido al libro de invitados!")

    # Solicitar al usuario un nombre
    nombre = input("Por favor, ingresa tu nombre: ")

    # Abrir el archivo en el modo especificado
    with open(archivo, modo) as f:
        # Escribir el nombre en el archivo junto con un salto de línea
        f.write(nombre + '\n')

    # Mostrar un saludo con el nombre del invitado
    print("Hola, {}! Gracias por tu visita.".format(nombre))


if __name__ == '__main__':
    import doctest
    doctest.testmod()