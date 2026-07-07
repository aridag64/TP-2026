from validaciones.validar import *
from tablas.tabla import *
from proyectos.proyecto import *
from estadisticas.estadisticas import *

usuarios_guardados = cargar_usuarios()

ingreso = False

while ingreso == False:
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")

    ingreso = validar_ingreso(usuarios_guardados, usuario, contraseña)

entro = validar_acceso(ingreso)

proyecto_actual = None

proyectos = cargar_proyectos()


while entro == True:
    print("a. PROYECTOS \nb. TABLAS \nc. VARIABLES \nd. MOSTRAR INFORMACIÓN \ne. ESTADÍSTICAS \nf. SALIR")
    menu = input("Ingrese su opcion: ")
    match menu:
            case "a":
                    proyecto_actual = sub_menu(proyectos)
            case "b":
                    if validar_proyecto(proyecto_actual):
                        mostrar_tablas(proyectos, proyecto_actual)
                        nombre_tabla = input("Ingrese nombre de la tabla: ")
                        if buscar_existe_nombre_tabla(nombre_tabla,proyectos,proyecto_actual):
                            generar_columnas = int(input("ingrese el numero de columnas deseadas : "))
                            generar_filas = int(input("ingrese el numero de filas deseadas : "))
                            matriz = generar_matriz(generar_filas, generar_columnas, "X")
                            cargar_matriz(matriz)
                            proyectos[proyecto_actual][nombre_tabla] = matriz
                            guardar_tabla(proyecto_actual, nombre_tabla, matriz)
                            guardar_proyectos(proyectos)
            case "c":
                    if validar_proyecto(proyecto_actual):
                        if buscar_existe_proyecto_tabla(proyectos,proyecto_actual):
                            mostrar_tablas(proyectos, proyecto_actual)
                            tabla = input("Ingrese el nombre de la tabla: ")
                            if buscar_existe_tabla(tabla,proyectos,proyecto_actual):
                                if tabla in proyectos[proyecto_actual]:
                                    modificar = input("queres modificar la tabla si/no : ")
                                    if modificar ==  "si":
                                        fila = int(input("Ingrese la fila a modificar: "))
                                        columna = int(input("Ingrese la columna a modificar: "))
                                        modificar_tabla(proyectos[proyecto_actual][tabla],fila,columna) 
                                        guardar_tabla(proyecto_actual, tabla, proyectos[proyecto_actual][tabla])
                                    elif modificar == "no":
                                        print("volviendo...")
            case "d":
                    if validar_proyecto(proyecto_actual):
                        if buscar_existe_proyecto_tabla(proyectos,proyecto_actual):
                            mostrar_tablas(proyectos, proyecto_actual)
                            tabla = input("Ingrese la tabla a mostrar: ")
                            if buscar_existe_tabla(tabla,proyectos,proyecto_actual):
                                mostrar_tabla(proyectos[proyecto_actual][tabla])  
            case "e":
                    if validar_proyecto(proyecto_actual):
                        if buscar_existe_proyecto_tabla(proyectos,proyecto_actual):    
                            mostrar_tablas(proyectos, proyecto_actual)
                            tabla = input("Ingrese la tabla a mostrar estadisticas: ")
                            mostrar_estadisticas(tabla,proyectos,proyecto_actual)
            case "f":
                print("saliendo....")
                entro = False
            case _:
                print("ingreso invalido")

