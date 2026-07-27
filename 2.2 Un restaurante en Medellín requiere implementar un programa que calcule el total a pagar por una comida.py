#Ejercicio:Un restaurante en Medellín requiere implementar un programa que calcule el total a pagar por una comida, considerando un descuento del 10% los lunes y miércoles para los clientes que consuman más de 50.000 pesos.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
cuenta=float(input("Escribe el valor de la ceunta: "))
dia=int(input("Si la compra fue hecha un lunes o un miercoles escribe 1, de lo contrario escribe 2: "))
if(dia==1) and (cuenta>=50000):
    descuento=cuenta*(10/100)
    total=cuenta-descuento
    print("El valor de la cuenta con un 10% de descuento es de:",total)
elif(cuenta>=0):
    print("El valor de la cuenta es de:",cuenta)
else:
    print("Error")
