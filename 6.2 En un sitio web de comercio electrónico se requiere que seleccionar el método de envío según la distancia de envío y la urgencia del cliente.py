#Ejercicio:En un sitio web de comercio electrónico se requiere que seleccionar el método de envío según la distancia de envío y la urgencia del cliente, si la urgencia es alta se debe imprimir "envio express", si la distancia del envio es menor a 120 km, será una un envio estándar y si la distancia es mayor a 120km será un "envio internacional"
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
distancia = float(input("Ingrese la distancia del envio en kilometros: "))
urgente = int(input("Si desea un envio urgente ingrese 1, de lo contrario ingrese 0: "))
if urgente == 1 and distancia <= 120:
    print("Metodo de envio seleccionado: Estandar Express")
elif urgente == 1 and distancia > 120:
    print("Metodo de envio seleccionado: Internacional Express")
elif distancia <= 120:
    print("Metodo de envio seleccionado: Estandar")
elif distancia > 120:
    print("Metodo de envio seleccionado: Internacional")
else:
    print("Los datos ingresados no son validos")
