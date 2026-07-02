from tablas.tabla import cargar_tabla

def crear_proyecto(proyectos:dict):

    nombre = input("Ingrese el nombre del proyecto: ")

    if nombre in proyectos:
        print("Ese proyecto ya existe.")

    else:
        proyectos[nombre] = {}
        guardar_proyectos(proyectos)
        print("Proyecto creado correctamente.")

def mostrar_proyectos(proyectos:dict):

    if len(proyectos) == 0:
        print("No existen proyectos.")
        return

    print("---PROYECTOS---")

    for proyecto in proyectos:
        print("-", proyecto)

def seleccionar_proyecto(proyectos:dict):

    mostrar_proyectos(proyectos)

    nombre = input("Proyecto: ")

    if nombre in proyectos:
        return nombre

    print("No existe.")


def guardar_proyectos(proyectos):

    with open("datos/proyectos.csv","w") as archivo:

        for proyecto in proyectos:
            if len(proyectos[proyecto]) == 0:
                archivo.write(proyecto + ";\n")
            else:
                for tabla in proyectos[proyecto]:

                    archivo.write(proyecto + ";" + tabla + "\n")


def cargar_proyectos():

    proyectos = {}

    with open("datos/proyectos.csv","r") as archivo:

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