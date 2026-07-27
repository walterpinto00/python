#Ejercicio:Una universidad en Bogotá, implementa un programa que determine si un estudiante es elegible para una beca. Para ello, se evalúan dos criterios: el promedio académico y el nivel de ingresos familiares. Si el promedio es mayor o igual a 4.0 y los ingresos son menores a 2 salarios mínimos, el estudiante recibe la beca completa. Si el promedio es menor a 4.0 pero los ingresos son menores a 3 salarios mínimos, recibe una beca parcial. En cualquier otro caso, no recibe beca.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
promedio=float(input("escriba el promedio academico: "))
ingresos=float(input("Escriba cuantos salarios minimos representan sus ingresos: "))
if(promedio>=4) and (ingresos<2):
    print("Felicidades obtuviste la beca completa: ")
elif(promedio<4) and (ingresos<3):
    print("Felicidades obtuviste la beca parcial: ")
else:
    print("No puedes obtener la beca")
