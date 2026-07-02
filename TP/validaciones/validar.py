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




def cargar_usuarios():

    usuarios = {}

    with open("usuarios.txt","r") as archivo:

        for linea in archivo:

            linea = linea.strip()
            datos = linea.split(";")
            usuario = datos[0]
            contraseña = datos[1]
            usuarios[usuario] = contraseña

    return usuarios


def registrar_usuario(usuarios):

    nuevo_usuario = input("Ingrese un usuario: ")

    if nuevo_usuario in usuarios:
        print("Ese usuario ya existe.")
    else:
        nueva_contraseña = input("Ingrese una contraseña: ")
        usuarios[nuevo_usuario] = nueva_contraseña

        with open("usuarios.txt","a") as archivo:
            archivo.write(f"{nuevo_usuario};{nueva_contraseña}\n")

        print("Usuario registrado correctamente.")


def validar_ingreso(usuarios):

    usuario = input("Ingrese nombre de usuario: ")

    contraseña = input("Ingrese contraseña: ")

    if usuario in usuarios:
        if usuarios[usuario] == contraseña:
            print("Bienvenido.")
            return True
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario inexistente.")
        registro = input("Quiere registrarse si/no : ")
        if registro == "si":
            registrar_usuario(usuarios)
        else:
            print("Cerrando...")
            return False
