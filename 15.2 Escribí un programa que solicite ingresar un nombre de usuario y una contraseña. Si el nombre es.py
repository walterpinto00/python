#Ejercicio:Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es "Gwenevere" y la contraseña es "excalibur", mostrar en pantalla "Usuario y contraseña correctos. Puede ingresar a Camelot". Si el nombre o la contraseña no coinciden, mostrar "Acceso denegado".
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
usuario = input("Ingrese su nombre de usuario: ")
clave = input("Ingrese su contrasena: ")
if usuario == "Gwenevere" and clave == "excalibur":
    print("Acceso concedido. Bienvenido/a a Camelot,", usuario)
else:
    print("Acceso denegado. El usuario o la contrasena son incorrectos")
