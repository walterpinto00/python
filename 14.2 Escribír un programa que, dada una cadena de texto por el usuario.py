#Ejercicio:Escribír un programa que, dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena es un número par, o False si no lo es.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
texto = input("Ingrese una cadena de texto: ")
cantidad = len(texto)
print("La cadena tiene", cantidad, "caracteres.")
if cantidad % 2 == 0:
    print("La cantidad de caracteres es PAR:", True)
else:
    print("La cantidad de caracteres es IMPAR:", False)
