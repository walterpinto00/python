#Ejercicio:En un sitio web de comercio electrónico se requiere que seleccionar el método de envío según la distancia de envío y la urgencia del cliente, si la urgencia es alta se debe imprimir “envio express”, si la distancia del envio es menor a 120 km, será una un envio estándar y si la distancia es mayor a 120km será un “envio internacional”
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
destancia=float(input("Esctriba la distancia del envio en kilometros: "))
envio=int(input("Si desa un envio urgente escriba 1: "))
if(envio==1) and (distancia<120):
    print("Eligio el envio estandar y express")
elif(distancia<120):
    print("Eligio el envio estandar")
elif(envio==1) and (distancia>120):
    print("Eligio el envio internacional y express")
elif(distancia>120):
    print("Eligio el envio internacional")
else:
    print("Error")
