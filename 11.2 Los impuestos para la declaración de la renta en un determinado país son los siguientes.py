#Ejercicio:Los impuestos para la declaración de la renta en un determinado país son los siguientes:
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
renta=float(input("Escriba la renta anual: "))
if(renta<2500000):
    print("El porcentaje de impuestos es del: 5%")
elif(renta>=2500000) and (renta<=3500000):
    print("El porcentaje de impuestos es del: 15%")
elif(renta>=3500001) and (renta<=4500000):
    print("El porcentaje de impuestos es del: 20%")
elif(renta>=4500001) and (renta<=6000000):
    print("Su porcentaje de impuestos es del: 30%")
else:
    print("El porcentaje de impuestos es del: 45%")
