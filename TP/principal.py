from validaciones.validar import *
from tablas.tabla import *
from proyectos.proyecto import *
from estadisticas.estadisticas import *

usuarios = cargar_usuarios()

entro = False

acceso = validar_ingreso(usuarios)

if acceso == True:
    entro = True
else:
    entro = False


proyectos = cargar_proyectos()

proyecto_actual = None


while entro == True:
    print("--- BIENVENIDO --- \na. PROYECTOS \nb. TABLAS " \
"\nc. VARIABLES \nd. MOSTRAR INFORMACIÓN \ne. ESTADÍSTICAS \nf. SALIR")
    menu = input("Bienvenido al programa ingrese su opcion: ")

    match menu:
            case "a":
                print("ingresaste a proyectos")
                print("Que desea hacer \n1.CREAR PROYECTO\n2.SELECCIONAR PROYECTO\n3.MOSTRAR PROYECTO\n4.VOLVER ")
                opciones = input("ingrese su opcion : ")
                match opciones:
                    case "1":
                        crear_proyecto(proyectos)
                    case "2":
                        proyecto_actual=seleccionar_proyecto(proyectos)
                        print("Proyecto seleccionado:", proyecto_actual)
                    case "3":
                        mostrar_proyectos(proyectos)
                    case "4":
                        print("Volviendo...")
                    case _:
                        print("ingrese una opcion valida")
            case "b":
                if proyecto_actual == None:
                    print("Primero debe seleccionar un proyecto")
                else:
                    print("Proyecto actual:", proyecto_actual)
                    print("ingresaste a tablas")
                    nombre_tabla = input("Ingrese nombre de la tabla: ")
                    if nombre_tabla in proyectos[proyecto_actual]:
                        print("Ya existe una tabla con ese nombre.")
                    else:
                        generar_columnas = int(input("ingrese el numero de columnas deseadas : "))
                        generar_filas = int(input("ingrese el numero de filas deseadas : "))
                        matriz = generar_matriz(generar_filas, generar_columnas, "X")
                        cargar_matriz(matriz)
                        proyectos[proyecto_actual][nombre_tabla] = matriz
                        guardar_tabla(proyecto_actual, nombre_tabla, matriz)
                        guardar_proyectos(proyectos)
            case "c":
                if proyecto_actual == None:
                    print("Primero debe seleccionar un proyecto")
                else:
                    print("ingresaste a variables")
                    if len(proyectos[proyecto_actual]) == 0:
                        print("Este proyecto no tiene tablas.")     
                    else:
                        mostrar_tablas(proyectos, proyecto_actual)
                        tabla = input("Ingrese el nombre de la tabla: ")
                        if tabla in proyectos[proyecto_actual]:
                            modificar = input("queres modificar la tabla si/no : ")
                            if modificar ==  "si":
                                modificar_tabla(proyectos[proyecto_actual][tabla]) 
                                guardar_tabla(proyecto_actual, tabla, proyectos[proyecto_actual][tabla])
                            elif modificar == "no":
                                print("volviendo...")
            case "d":
                if proyecto_actual == None:
                    print("Primero debe seleccionar un proyecto")
                else:
                    print("ingresaste a mostrar")
                    if len(proyectos[proyecto_actual]) == 0:
                        print("Este proyecto no tiene tablas.")
                    else:
                        mostrar_tablas(proyectos, proyecto_actual)
                        tabla = input("Ingrese la tabla a mostrar: ")
                        if tabla in proyectos[proyecto_actual]:
                            mostrar_tabla(proyectos[proyecto_actual][tabla])  
                        else:
                            print("La tabla no existe.") 
            case "e":
                if proyecto_actual == None:
                    print("Primero debe seleccionar un proyecto")
                else:
                    print("ingresaste a estadistica")
                    if len(proyectos[proyecto_actual]) == 0:
                        print("Este proyecto no tiene tablas.")
                    else:
                        print(proyectos)
                        mostrar_tablas(proyectos, proyecto_actual)
                        tabla = input("Ingrese la tabla a mostrar estadicas: ")
                        conteo = contar(proyectos[proyecto_actual][tabla])
                        mayor = dar_maximo(proyectos[proyecto_actual][tabla])
                        menor = dar_minimo(proyectos[proyecto_actual][tabla])
                        promedio = dar_promedio(proyectos[proyecto_actual][tabla])
                        varianza = dar_varianza(proyectos[proyecto_actual][tabla])
                        coeficiente = dar_coeficiente_variacion(proyectos[proyecto_actual][tabla])
                        desvio = dar_desvio_estandar(proyectos[proyecto_actual][tabla])
                        #mediana = dar_mediana(proyectos[proyecto_actual][tabla])
                        corte_c = int(input("Ingrese el cuartil (1 al 3): "))
                        cuartil = dar_posicion(proyectos[proyecto_actual][tabla],4,corte_c)
                        corte_d  = int(input("Ingrese el decil (1 al 9): "))
                        decil = dar_posicion(proyectos[proyecto_actual][tabla],10,corte_d)
                        print(f"Conteo de datos: {conteo}.\nEl promedio es:{promedio}")
                        print(f"Mayor valor:{mayor}\nMenor valor:{menor}")
                        print(f"Varianza:{varianza}")
                        print(f"Coeficiente:{coeficiente}")
                        print(f"Desvio estandar:{desvio}")
                        #print(f"Mediana:{mediana}")
                        print(f"Cuartil:{cuartil}")
                        print(f"Decil:{decil}") 
            case "f":
                print("saliendo....")
                entro = False
            case _:
                print("ingreso invalido")

