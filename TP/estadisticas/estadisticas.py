def calcular_maximo(matriz:list) -> float:

    """ La variable maximo es el primer indice. Recorre 
    la matriz y si encuentra un valor mas grande que 
    esa variable, se declara el nuevo maximo. 
    """

    maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento

    return maximo

def calcular_minimo(matriz:list) -> float:

    """Funciona igual que maximo, solo que la variable se 
    reemplaza si encuentra un valor menor
    """

    minimo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento < minimo:
                minimo = elemento

    return minimo

def contar(matriz:list) -> dict:
    frecuencias = {}

    for fila in matriz:
        for dato in fila:
            if dato in frecuencias:
                frecuencias[dato] += 1
            else:
                frecuencias[dato] = 1

    return frecuencias


def calcular_promedio(matriz:list) -> float:

    """Usando la lista armada en dar_numeros, sumamos esos valores
    y los dividimos por la cantidad de datos (que es el len de la lista).
    """

    datos = calcular_numeros(matriz)

    suma = 0

    for numero in datos:
        suma += numero

    return suma / len(datos)


def calcular_numeros(matriz:list) -> list:


    """dar_numeros salta la fila 0 (que suele tener strings por ser nombres de columnas)
    y revisa si cada valor es un entero mediante Ascii. Si lo es, ingresa a 
    la lista. Funcion reutilizable para el resto de estadisticas.
    """


    numeros = []

    for fila in matriz[1:]:
        for dato in fila:

            es_numero = True

            for i in range(len(dato)):
                codigo = ord(dato[i])

                if 48 <= codigo <= 57:
                    numeros.append(int(dato))

                else:
                    es_numero = False
                    break

    return numeros


def calcular_varianza(matriz:list) -> float:
    """Al valor de dar_varianza se lo eleva a 0.5,
    que es lo mismo que hacerle la raiz cuadrada.
    """

    datos = calcular_numeros(matriz)
    media = calcular_promedio(matriz)
    suma = 0

    for numero in datos:
        suma += (numero - media) ** 2

    return suma / len(datos)


def dar_desvio_estandar(matriz):

    return calcular_varianza(matriz) ** 0.5



def calcular_coeficiente_variacion(matriz:list) -> int:

    """el desvio estandar se divide por el promedio y al
    resultado se lo multiplica por 100"""

    media = calcular_promedio(matriz)

    desvio = dar_desvio_estandar(matriz)

    return (desvio / media) * 100


def ordenar_burbujeo(matriz:list) -> list:

    """los usamos para acomodar y despues ver las posciones. Va 
    acomodando cuando ve que un valor es mas gradne que el indice 
    comparado
    """

    lista = calcular_numeros(matriz)

    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista


def calcular_posicion(matriz:list, divisiones:int, k:int) -> any:

    """posicion multiplica el largo +1 y divide por el parametro
        que depende si es cuartil o decil. 
    """

    datos = ordenar_burbujeo(matriz)

    n = len(datos)

    posicion = int((k * (n + 1)) / divisiones)

    if posicion < 1:
        posicion = 1

    if posicion > n:
        posicion = n

    return datos[posicion - 1]


def mostrar_estadisticas(tabla:str,proyectos:dict,proyecto_actual:str) -> None:

    """muestra en pantalla  todas las estadisticas
    """
    
    conteo = contar(proyectos[proyecto_actual][tabla])
    mayor = calcular_maximo(proyectos[proyecto_actual][tabla])
    menor = calcular_minimo(proyectos[proyecto_actual][tabla])
    promedio = calcular_promedio(proyectos[proyecto_actual][tabla])
    varianza = calcular_varianza(proyectos[proyecto_actual][tabla])
    coeficiente = calcular_coeficiente_variacion(proyectos[proyecto_actual][tabla])
    desvio = dar_desvio_estandar(proyectos[proyecto_actual][tabla])
    corte_c = int(input("Ingrese el cuartil (1 al 3): "))
    cuartil = calcular_posicion(proyectos[proyecto_actual][tabla],4,corte_c)
    corte_d  = int(input("Ingrese el decil (1 al 9): "))
    decil = calcular_posicion(proyectos[proyecto_actual][tabla],10,corte_d)

    print(f"""Conteo de datos: {conteo}
        El promedio es: {promedio}
        Mayor valor: {mayor}
        Menor valor: {menor}
        Varianza: {varianza}
        Coeficiente: {coeficiente}
        Desvío estándar: {desvio}
        Cuartil: {cuartil}
        Decil: {decil}""")



