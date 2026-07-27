#Ejercicio:Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
letra=input("Escriba una letra: ")
if(len(letra)>1):
    print("No se puede procesar el dato")
elif(letra=="a") or (letra=="e") or (letra=="i") or (letra=="o") or (letra=="u"):
    print("Es vocal")
else:
    print("No es vocal")
