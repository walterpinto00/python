#Ejercicio:Escribír un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
palabra1=input("Escriba la primera palabra: ")
palabra2=input("Escriba la segunda palabra: ")
if(palabra1<palabra2):
    resultado=True
    print(resultado)
elif(palabra1>palabra2):
    resultado=False
    print(resultado)
else:
    print("Error")
