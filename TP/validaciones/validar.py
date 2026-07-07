def validar_rangos(num:int,minimo:int,maximo:int) -> bool:


    """si el numero esta esta entre minimo y maximo 
        retorna true
    """
    
    if num >= minimo and num <= maximo:
        return True
    else:
        return False



def determinar_paridad(num : int) -> bool:

    """si el resto de la divison es 0 retorna par (true) y sino 
    retorna false (impar)
    """

    if num % 2 == 0:
        return True
    else:
        return False



def determinar_primo(numero) ->bool:


    """Usa un contador, si hay mas de 2 divisores no es primo
        retorna un bool
    """


    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        return True

    else:
        return False



def determinar_multiplo(num:int,num2:int) -> bool:

    """si el resto es 0 entre ambos numeros , es multiplo
        retorna un bool
    """

    if num2 % num == 0:
        return True
    else:
        return False


def determinar_recursividad (num:int):

    """va restando de a 1, salvo que sea el 1
    """

    if num == 1:
        return 1
    else:
        return determinar_recursividad(num - 1)



def validar_acceso(acceso:bool)->bool:

    """
        ingresamos por parametro un bool
        verificamos si es true
    Returns:
        retorna un bool
    """

    if acceso == True:
        return True
    else:
        return False



def validar_proyecto(proyecto_actual:dict) -> bool:

    """
        ingresamos por parametro un diccionario de nuestro proyecto actual
        verificamos que no sea None
    Returns:
        retorna un bool
    """ 

    if proyecto_actual == None:
        print("Primero debe seleccionar un proyecto")
        return False
    else:
        return True


def buscar_existe_proyecto(proyectos:dict) -> bool:
    """
        ingresamos por parametro un diccionario de nuestros proyectos
        verificamos que no este vacio
    Returns:
        retorna un bool
    """
    
    if len(proyectos) == 0:
        print("No existen proyectos")
        return False
    else:
        return True


def buscar_existe_nombre_proyecto(nombre:str,proyectos:dict) -> bool:
    """
        ingresamos por parametro nombre y un diccionario de proyectos
        verifica si el nombre pasado por parametro se encuentra en el diccionario 
    Returns:
        retorna un bool
    """

    if nombre in proyectos:
        print("Ese proyecto ya existe.")
        return False
    else:
        return True

def buscar_existe_nombre_tabla(nombre_tabla:str,proyectos:dict,proyecto_actual:str) -> bool:
    """
        recibe por parametro el nombre de una tabla, el diccionario de proyectos y  el proyecto actual
        verifica si el pnombre de la tabla  existe dentro del diccionario
    Returns:
        bool: false si el nombre de la tabla existe, true en caso contrario

    """

    if nombre_tabla in proyectos[proyecto_actual]:
        print("Ya existe una tabla con ese nombre")
        return False
    else:
        return True


def buscar_existe_proyecto_tabla(proyectos:dict,proyecto_actual:str) -> bool:

    """
        recibe por parametro el diccionario de proyectos y  el proyecto actual
        verifica si el proyecto tiene tablas 
    Returns:
        bool: true si tiene tablas , false en caso contrario    
    """

    if len(proyectos[proyecto_actual]) == 0:
        print("Este proyecto no tiene tablas.")
        return False
    else:
        return True
    

def buscar_existe_tabla(tabla:str,proyectos:dict,proyecto_actual:str) -> bool:
    """
        recibe por parametro una tabla, el diccionario de proyectos y  el proyecto actual
        verifica si  la tabla  existe dentro del diccionario
    Returns:
        bool: true si la tabla existe, false en caso contrario
    """

    if tabla in proyectos[proyecto_actual]:
        return True                                
    else:
        print("La tabla no existe.")
        return False


def cargar_usuarios() -> dict:

    """
        abrimos usuarios.txt como archivo
        recorremos archivo linea por linea
        cargamos usuarios y contraseñas
    Returns:
        retorna el diccionario usuarios
    """

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
    """
        recibe por parametro el diccionario usuarios
        pedimos el ingreso de un nuevo usuario
        pedimos el ingreso de una nueva contraseña
        abrimos usuarios.txt como archivo
        esribimos el archivo con los nuevos datos de registro
        no retorna nada
    """

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

    """
        recibe por parametro un diccionario de usuarios
        recibe por parametro el ingreso de usuario y contraseña
        verificamos si el usuario y la contraseña ingresada coincide con el diccionario de usuarios
        si coincide retornamos true , sino preguntamos si quiere registrarse
    Returns:
        retorna False
    """

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
