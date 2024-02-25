def consulta_raw(archivo):
    # Abrir el archivo en modo lectura
    f = open(archivo, 'r')
    # Leer todo el contenido del archivo
    contenido = f.read()
    # Cerrar el archivo
    f.close()
    # Mostrar el contenido por pantalla
    print(contenido)

# Llamada a la función para mostrar el contenido del archivo consulta.txt
consulta_raw('consulta.txt')

def consulta_lines(archivo):
    try:
        # Abre el archivo en modo lectura
        f = open(archivo, 'r')
        # Itera sobre cada línea del archivo
        for linea in f:
            # Muestra el contenido de la línea
            print(linea, end='')
    except FileNotFoundError:
        print("El archivo no se encontró.")
    finally:
        # Cierra el archivo al finalizar
        if f:
            f.close()

# Ejemplo de uso:
archivo = 'consulta.txt'
consulta_lines(archivo)


def consulta_lines_with(archivo):
    # Lista para almacenar las líneas del archivo
    lineas = []

    # Abriendo el archivo usando la sentencia with
    with open(archivo, 'r') as f:
        # Iterando sobre cada línea del archivo
        for linea in f:
            # Añadiendo cada línea a la lista
            lineas.append(linea.strip())  # Eliminando espacios en blanco al inicio y al final

    # Mostrando el contenido de las líneas
    for linea in lineas:
        print(linea)


# Uso de la función consulta_lines_with
archivo = 'consulta.txt'
consulta_lines_with(archivo)