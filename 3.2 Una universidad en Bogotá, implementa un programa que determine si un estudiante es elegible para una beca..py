#Ejercicio:Una universidad en Bogotá, implementa un programa que determine si un estudiante es elegible para una beca. Para ello, se evalúan dos criterios: el promedio académico y el nivel de ingresos familiares. Si el promedio es mayor o igual a 4.0 y los ingresos son menores a 2 salarios mínimos, el estudiante recibe la beca completa. Si el promedio es menor a 4.0 pero los ingresos son menores a 3 salarios mínimos, recibe una beca parcial. En cualquier otro caso, no recibe beca.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
promedio = float(input("Ingrese el promedio academico del estudiante: "))
ingresos = float(input("Ingrese cuantos salarios minimos representan los ingresos familiares: "))
if promedio >= 4.0 and ingresos < 2:
    print("Felicitaciones! El estudiante es elegible para la beca completa")
elif promedio < 4.0 and ingresos < 3:
    print("El estudiante es elegible para una beca parcial")
else:
    print("Lo sentimos, el estudiante no cumple los requisitos para obtener ninguna beca")
