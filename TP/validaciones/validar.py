def validar_rangos(num:int,minimo:int,maximo:int) -> bool:
    
    if num >= minimo and num <= maximo:
        print("cumple la condicion")
        return True
    else:
        print("no cumple la condicion")
        return False



def determina_paridad(num : int) -> bool:

    if num % 2 == 0:
        print("es par")
        return True
    else:
        print("no es par")
        return False



def determina_primo(numero) ->bool:
#solo divisible por el y por 1:
    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        return True

    else:
        return False



def determina_multiplo(num:int,num2:int) -> bool:

    if num2 % num == 0:
        print("es multiplo")
        return True
    else:
        print("no es multiplo")
        return False


def determinar_recursividad (num:int):

    if num == 1:
        return 1
    else:
        return determinar_recursividad(num - 1)



def validar_acceso(acceso:bool)->bool:

    if acceso == True:
        return True
    else:
        return False



def validar_proyecto(proyecto_actual:dict) -> bool:

    if proyecto_actual == None:
        print("Primero debe seleccionar un proyecto")
    else:
        return True




def existe_proyecto(proyectos:dict) -> bool:
    
    if len(proyectos) == 0:
        print("No existen proyectos")
    else:
        return True



def existe_nombre_proyecto(nombre:str,proyectos:dict) -> bool:
    if nombre in proyectos:
        print("Ese proyecto ya existe.")
    else:
        return True

def existe_nombre_tabla(nombre_tabla:str,proyectos:dict,proyecto_actual) -> bool:

    if nombre_tabla in proyectos[proyecto_actual]:
        print("Ya existe una tabla con ese nombre")
    else:
        return True


def existe_proyecto_tabla(proyectos:dict,proyecto_actual:str) -> bool:

    if len(proyectos[proyecto_actual]) == 0:
        print("Este proyecto no tiene tablas.")
    else:
        return True
    

def existe_tabla(tabla:str,proyectos:dict,proyecto_actual:str) -> bool:

    if tabla in proyectos[proyecto_actual]:
        return True                                
    else:
        print("La tabla no existe.") 




def cargar_usuarios():

    usuarios = {}

    with open("TP/Usuarios/usuarios.txt","r") as archivo:

        for linea in archivo:

            linea = linea.strip()      
            datos = linea.split(";")
            usuario = datos[0]
            contraseña = datos[1]
            usuarios[usuario] = contraseña

    return usuarios


def registrar_usuario(usuarios:dict) -> None:

    nuevo_usuario = input("Ingrese un usuario: ")

    if nuevo_usuario in usuarios:
        print("Ese usuario ya existe.")
    else:
        nueva_contraseña = input("Ingrese una contraseña: ")
        usuarios[nuevo_usuario] = nueva_contraseña

        with open("TP/Usuarios/usuarios.txt","a") as archivo:
            archivo.write(f"{nuevo_usuario};{nueva_contraseña}\n")

        print("Usuario registrado correctamente.")


def validar_ingreso(usuarios:dict,usuario:str,contraseña:int) -> bool:

    if usuario in usuarios:
        if usuarios[usuario] == contraseña:
            print("Ingreso exitoso.")
            return True

        print("Contraseña incorrecta")
        return False

    print("Usuario inexistente.")
    registro = input("¿Quiere registrarse? (si/no): ")

    if registro == "si":
        registrar_usuario(usuarios)
        print("Ahora vuelva a iniciar sesión")

    return False
