#Ejercicio:Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    print("El cliente tiene", edad, "años. La entrada es GRATUITA")
elif edad >= 4 and edad <= 18:
    print("El cliente tiene", edad, "años. El precio de la entrada es: 5 euros")
elif edad > 18:
    print("El cliente tiene", edad, "años. El precio de la entrada es: 10 euros")
else:
    print("La edad ingresada no es valida")
