#Ejercicio:Escribír un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
print("Comparando:", palabra1, "vs", palabra2)
if palabra1 < palabra2:
    print("La primera palabra va antes alfabeticamente:", True)
elif palabra1 > palabra2:
    print("La primera palabra va despues alfabeticamente:", False)
else:
    print("Las dos palabras son iguales")
