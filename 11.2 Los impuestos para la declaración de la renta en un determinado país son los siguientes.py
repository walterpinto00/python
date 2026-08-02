#Ejercicio:Los impuestos para la declaración de la renta en un determinado país son los siguientes:
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
renta = float(input("Ingrese su renta anual en pesos: "))
if renta < 2500000:
    porcentaje = 5
    print("Su renta es de", renta, "pesos. El porcentaje de impuestos es del:", porcentaje, "%")
elif renta >= 2500000 and renta <= 3500000:
    porcentaje = 15
    print("Su renta es de", renta, "pesos. El porcentaje de impuestos es del:", porcentaje, "%")
elif renta >= 3500001 and renta <= 4500000:
    porcentaje = 20
    print("Su renta es de", renta, "pesos. El porcentaje de impuestos es del:", porcentaje, "%")
elif renta >= 4500001 and renta <= 6000000:
    porcentaje = 30
    print("Su renta es de", renta, "pesos. El porcentaje de impuestos es del:", porcentaje, "%")
else:
    porcentaje = 45
    print("Su renta es de", renta, "pesos. El porcentaje de impuestos es del:", porcentaje, "%")
