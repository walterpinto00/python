#Ejercicio:Un restaurante en Medellín requiere implementar un programa que calcule el total a pagar por una comida, considerando un descuento del 10% los lunes y miércoles para los clientes que consuman más de 50.000 pesos.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
cuenta = float(input("Ingrese el valor total de la cuenta: "))
dia = int(input("Si la compra fue realizada un lunes o miercoles ingrese 1, de lo contrario ingrese 0: "))
if dia == 1 and cuenta >= 50000:
    descuento = cuenta * (10 / 100)
    total = cuenta - descuento
    print("Tiene un descuento del 10%. El total a pagar es:", total, "pesos")
elif cuenta > 0:
    print("No aplica descuento. El total a pagar es:", cuenta, "pesos")
else:
    print("El valor ingresado no es valido")
