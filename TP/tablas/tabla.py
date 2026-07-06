def generar_matriz(filas: int,columnas: int,elemento_default : any = 0) -> list:

    """
        ingresamos filas y columnas por parametro
        recorremos las filas para crear las columnas multiplicando el elemento default
        crea la matriz
    Return:
        matriz
    """
    
    matriz = []

    for _ in range(filas):

        fila = [elemento_default] * columnas

        matriz.append(fila)

    return matriz


def cargar_matriz(matriz:list) -> list:

    """
        pasamos por parametro la matriz generada con la funcion generar_matriz
        recorre las filas y columnas y pide el ingreso de sus datos
    Returns:
        matriz con datos de filas y columnas
    """


    for j in range(len(matriz[0])):
        matriz[0][j] = input(f"Ingrese el nombre de las columnas {j+1}: ")

    for i in range(1, len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = input(f"ingrese {matriz[0][j]} en (fila {i}): ")

    return matriz



def modificar_tabla(matriz: list, fila: int, columna: int) -> list:

    cantidad_filas = len(matriz)
    cantidad_columnas = len(matriz[0])

    if 0 <= fila < cantidad_filas and 0 <= columna < cantidad_columnas:

        print(f"Valor actual: {matriz[fila][columna]}")

        nuevo_valor = input("Ingrese el nuevo valor: ")

        matriz[fila][columna] = nuevo_valor

        print("Modificación realizada")

    else:
        print("Fila o columna inválida")

    return matriz






def mostrar_tabla(matriz) -> None:

    """_
        pasamos por parametro la matriz cargada tanto si esta modificada como si no
        verificamos que la matriz no este vacia
        observamos la longitud de la matriz
        preguntamos si quiere ver todas las columnas
        si quiere ver todas las columnas se las muestra
        si no quiere ver todas le preguntamos cuales quiere que se muestren
    Returns:
        no retorna nada
    """

    if len(matriz) == 0:
        print("la tabla esta vacia")
        return

    cantidad_columnas = len(matriz[0])
    cantidad_filas = len(matriz)

    columnas_activas = [False] * cantidad_columnas

    visualizar_columnas= input("¿Desea ver todas las columnas? si/no : ")

    if  visualizar_columnas == "si":
        for i in range(cantidad_filas):
            for j in range(cantidad_columnas):
                columnas_activas[j] = True
                if columnas_activas[j]:
                    print(matriz[i][j], end="\t")
            print("")
    elif visualizar_columnas == "no":

        print("Seleccione las columnas que quiere ver:")

        for j in range(cantidad_columnas):
                respuesta = input(f"¿Mostrar columna '{matriz[0][j]}'? si/no: ")
                if respuesta == "si":
                    columnas_activas[j] = True
        
        for i in range(cantidad_filas):
            for j in range(cantidad_columnas):
                if columnas_activas[j]:
                    print(f"{matriz[i][j]:<10}", end="")
            print()
    else:
        print("ingrese una respuesta valida")


def mostrar_tablas(proyectos, proyecto_actual) -> None:
    """
        pasamos por parametro los proyectos y el proyecto actual
        mostramos las tablas disponibles en el proyecto actual
        no retorna nada
    """

    print("---TABLAS DEL PROYECTO---")

    for tabla in proyectos[proyecto_actual].keys():

        print(tabla)


def guardar_tabla(nombre_proyecto:str, nombre_tabla:str, matriz:list) -> None:

    """
        pasamos por parametro el nombre dado al proyecto al igual que el nombre de la tabla y la matriz
        se crea un csv con el nombre del proyecto y el nombre de la tabla
        se abre el csv y se guarda los datos dados por la matriz
        no retorna nada
    """

    nombre_archivo = f"datos/{nombre_proyecto}-{nombre_tabla}.csv"

    with open(nombre_archivo, "w") as archivo:

        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                archivo.write(matriz[i][j])
                if j < len(matriz[i]) - 1:
                    archivo.write(";")

            archivo.write("\n")


def cargar_tabla(nombre_proyecto:str, nombre_tabla:str) -> list:

    """
        pasamos por parametro el nombre del proyecto y el nombre de la tabla
        abrimos el scv y lo recorremos para mostrar sus datos
    Returns:
        matriz guardada en el csv
    """

    matriz = []

    nombre_archivo = f"datos/{nombre_proyecto}-{nombre_tabla}.csv"

    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:

            linea = linea.strip()
            fila = linea.split(";")
            matriz.append(fila)

    return matriz


