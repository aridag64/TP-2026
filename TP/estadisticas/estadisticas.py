'''
contar devuelve un diccionario con frecuencias.
maximo y minimo recorre la matriz y reemplaza el valor inicial.


obtener_burbujeo es la forma de ordenar. Nos sirve para usar
despes en mediana y dar_posicion, ya que son funciones que requieren
una lista ordenada.

dar_posicion se usa para decil y cuartil por igual, el parametro 2
es lo que cambia en el menu y el parametro 3 es elegido por 
el usuario.
'''

def dar_maximo(matriz):

    maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento

    return maximo

def dar_minimo(matriz):

    minimo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento < minimo:
                minimo = elemento

    return minimo

def contar(matriz):
    frecuencias = {}

    for fila in matriz:
        for dato in fila:
            if dato in frecuencias:
                frecuencias[dato] += 1
            else:
                frecuencias[dato] = 1

    return frecuencias


def dar_promedio(matriz):

    datos = dar_numeros(matriz)

    suma = 0

    for numero in datos:
        suma += numero

    return suma / len(datos)


def dar_numeros(matriz):

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


def dar_varianza(matriz):

    datos = dar_numeros(matriz)
    media = dar_promedio(matriz)
    suma = 0

    for numero in datos:
        suma += (numero - media) ** 2

    return suma / len(datos)


def dar_desvio_estandar(matriz):

    return dar_varianza(matriz) ** 0.5



def dar_coeficiente_variacion(matriz):

    media = dar_promedio(matriz)

    desvio = dar_desvio_estandar(matriz)

    return (desvio / media) * 100


def ordenar_burbujeo(matriz):

    lista = dar_numeros(matriz)

    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista


#def dar_mediana(datos):

#    datos = ordenar_burbujeo(datos)

#    n = len(datos)

#    if n % 2 == 0:
#        return (datos[n//2+1] + datos[n//2]) / 2
#    else:
#        return [datos(n+1)//2]


def dar_posicion(matriz, divisiones, k):

    datos = ordenar_burbujeo(matriz)

    n = len(datos)

    posicion = int((k * (n + 1)) / divisiones)

    if posicion < 1:
        posicion = 1

    if posicion > n:
        posicion = n

    return datos[posicion - 1]





