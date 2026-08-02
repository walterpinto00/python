#Ejercicio:En un servicio de taxi en Barranquilla, implementa un programa que calcule la tarifa a cobrar. Si la distancia es menor o igual a 5 km, la tarifa es de 5000 pesos. Si la distancia es mayor a 5 km, se cobra un adicional de 2000 pesos por cada kilómetro extra. Además, si el viaje es de noche (después de las 8 p.m.), se aplica un recargo del 20%.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
distancia = float(input("Ingrese la distancia del viaje en kilometros: "))
hora = int(input("Ingrese la hora del viaje en formato 24h (0-23): "))
if distancia <= 5:
    tarifa = 5000
    print("Distancia:", distancia, "km. Tarifa base: 5000 pesos")
else:
    tarifa = 5000 + (distancia - 5) * 2000
    print("Distancia:", distancia, "km. Tarifa base:", tarifa, "pesos")
if hora >= 20:
    recargo = tarifa * (20 / 100)
    tarifa_final = tarifa + recargo
    print("Viaje nocturno: recargo del 20% aplicado.")
    print("Tarifa final a pagar:", tarifa_final, "pesos")
else:
    print("Viaje diurno: sin recargo adicional.")
    print("Tarifa final a pagar:", tarifa, "pesos")
