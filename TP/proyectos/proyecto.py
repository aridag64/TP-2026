from tablas.tabla import cargar_tabla
from validaciones.validar import *

def crear_proyecto(nombre:str,proyectos:dict) -> None:

    """
        ingresamos por parametro un diccionario proyectos
        guardamos el diccionario proyectos con el nombre pasado por parametro en un csv
        no retorna nada
    """ 
    proyectos[nombre] = {}
    guardar_proyectos(proyectos)
    print("Proyecto creado correctamente")

def mostrar_proyectos(proyectos:dict) -> None:

    """
        ingresamos por parametro un diccionario proyectos
        muestra por pantalla los proyectos disponibles
        no retorna nada
    """

    if buscar_existe_proyecto(proyectos):
        print("---PROYECTOS---")
        for proyecto in proyectos:
            print("->", proyecto)

def seleccionar_proyecto(nombre:str,proyectos:dict) -> str:
    """
        ingresamos por parametro un diccionario proyectos
        pedimos ingreso de nombre del proyecto
    Returns:
        retorna nombre del proyecto
    """

    if nombre in proyectos:
        return nombre 
    else:
        print("No existe")


def guardar_proyectos(proyectos:dict) -> None:
    """
        ingresamos por parametro un diccionario proyectos
        abrimos el archivo proyectos.csv como archivo
        recorremos el archivo
        guardamos los datos en el archivo
        no retorna nada
    """

    with open("TP/datos/proyectos.csv","w") as archivo:

        for proyecto in proyectos:
            if len(proyectos[proyecto]) == 0:
                archivo.write(proyecto + ";\n")
            else:
                for tabla in proyectos[proyecto]:
                    archivo.write(proyecto + ";" + tabla + "\n")


def cargar_proyectos() -> dict:

    """
        carga los proyectos almacenados en 'proyectos.csv'. Si un proyecto
        tiene tablas asociadas, las carga utilizando la función
        `cargar_tabla()`.

    Returns:
        retorna diccionario con todos los proyectos y sus tablas
    """

    proyectos = {}

    with open("TP/datos/proyectos.csv","r") as archivo:

        for linea in archivo:

            linea = linea.strip()
            datos = linea.split(";")
            proyecto = datos[0]
            if proyecto not in proyectos:
                proyectos[proyecto] = {}
            if len(datos) > 1 and datos[1] != "":
                tabla = datos[1]

                proyectos[proyecto][tabla] = cargar_tabla(proyecto, tabla)

    return proyectos



def sub_menu(proyectos:dict) -> str:
    continuar = True
    while continuar == True:
        print("1.CREAR PROYECTO \n2.SELECCIONAR PROYECTO \n3.MOSTRAR PROYECTO \n4.VOLVER ")
        opciones = input("Ingrese su opcion : ")
        match opciones:
                case "1":
                    nombre = input("Ingrese el nombre del proyecto: ")
                    buscar_existe_nombre_proyecto(nombre,proyectos)
                    crear_proyecto(nombre,proyectos)
                case "2":
                    mostrar_proyectos(proyectos)
                    nombre = input("Selecciona proyecto: ")
                    proyecto_actual = seleccionar_proyecto(nombre,proyectos)
                    print("Proyecto seleccionado:", proyecto_actual)
                case "3":
                    mostrar_proyectos(proyectos)
                case "4":
                    print("Volviendo...")
                    continuar = False
                case _:
                    print("ingrese una opcion valida")
    return proyecto_actual