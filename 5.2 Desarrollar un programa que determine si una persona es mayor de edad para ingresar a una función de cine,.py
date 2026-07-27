#Ejercicio:Desarrollar un programa que determine si una persona es mayor de edad para ingresar a una función de cine, y en caso contrario, le informe que necesita la compañía de un adulto
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
edad=int(input("Escriba su edad: "))
if(edad>=18):
    print("Felicidades, cuenta con la edad suficiente")
elif(edad<18) and (edad>0):
    print("No puede asistir solo, es necesario que asista con un mayor de edad")
else:
    print("Error")
