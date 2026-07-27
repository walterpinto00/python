#Ejercicio:En un programa de impuestos en Colombia, calcula el impuesto a pagar según el salario anual y el estado civil del contribuyente. Si el salario anual es menor o igual a 10 millones de pesos, no se aplica impuesto. Si el salario anual está entre 10 y 20 millones de pesos, se aplica un impuesto del 10% para solteros y del 5% para casados. Si el salario anual es mayor a 20 millones de pesos, se aplica un impuesto del 20% para solteros y del 15% para casados.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
salario=float(input("Escribe el salario anual: "))
estado=float(input("Si su estado civil es soltero escriba 1, si es casado escriba 2: "))
if(salario<=10000000):
    print("No tiene que pagar impuestos: ")
elif(salario>10000000) and (salario>=20000000) and (estado==1):
    impuesto=salrio*(10/100)
    print("El valor a pagar es de:",impuestos)

elif(salario>10000000) and (salario>=20000000) and (estado==2):
    impuesto=salrio*(5/100)
    print("El valor a pagar es de:",impuestos)
elif(salario>20000000) and (estado==1):
    impuesto=salario*(20/100)
    print("El valor a pagar es de:",impuestos)
elif(salario>20000000) and (estado==2):
    impuesto=salario*(15/100)
    print("El valor a pagar es de:",impuestos)
else:
    print("Error")
