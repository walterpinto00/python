#Ejercicio:Escribír un programa que, dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena es un número par, o False si no lo es.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
texto=input("Escriba un texto: ")
cantidad=len(texto)
if(cantidad%2==0):
    resultado=True
    print(resultado)
else:
    resultado=False
    print(resultado)
