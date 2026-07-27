#Ejercicio:Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
usuario=input("Escriba el nombre de usuario: ")
clave=input("Escriba la contraseña: ")
if(usuario=="Gwenevere") and (clave=="excalibur"):
    print("Usuario y contraseña son correctos, Puede ingresar a Camelot")
else:
    print("Acceso denegado")
