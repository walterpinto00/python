#Ejercicio:En un servicio de taxi en Barranquilla, implementa un programa que calcule la tarifa a cobrar. Si la distancia es menor o igual a 5 km, la tarifa es de 5000 pesos. Si la distancia es mayor a 5 km, se cobra un adicional de 2000 pesos por cada kilómetro extra. Además, si el viaje es de noche (después de las 8 p.m.), se aplica un recargo del 20%.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
distancia=float(input("Escriba la distancia del viaje en km: "))
hora=int(input("Escriba la hora del viaje (0-23): "))
if(distancia<=5):
    tarifa=5000
    print("La distancia es menor o igual a 5 km, la tarifa base es 5000 pesos")
else:
    tarifa=5000+(distancia-5)*2000
    print("La distancia es mayor a 5 km, la tarifa base es:",tarifa,"pesos")
if(hora>=20):
    tarifas=tarifa*(20/100)
    print("El viaje es de noche, se aplica un recargo del 20%")
    print("La tarifa con recargo es:",tarifas,"pesos")
else:
    print("El viaje es de día, no se aplica recargo")
    print("La tarifa final es:",tarifas,"pesos")
