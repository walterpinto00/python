#Ejercicio:Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje "Es vocal". Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
letra = input("Ingrese una letra para verificar si es vocal: ")
if len(letra) > 1:
    print("Solo se puede ingresar un caracter. No es posible procesar el dato ingresado")
elif letra.lower() in ("a", "e", "i", "o", "u"):
    print("La letra '", letra, "' es una VOCAL", sep="")
else:
    print("La letra '", letra, "' es una CONSONANTE", sep="")
