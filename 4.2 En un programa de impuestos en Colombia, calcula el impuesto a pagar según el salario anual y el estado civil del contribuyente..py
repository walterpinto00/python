#Ejercicio:En un programa de impuestos en Colombia, calcula el impuesto a pagar según el salario anual y el estado civil del contribuyente. Si el salario anual es menor o igual a 10 millones de pesos, no se aplica impuesto. Si el salario anual está entre 10 y 20 millones de pesos, se aplica un impuesto del 10% para solteros y del 5% para casados. Si el salario anual es mayor a 20 millones de pesos, se aplica un impuesto del 20% para solteros y del 15% para casados.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
salario = float(input("Ingrese el salario anual en pesos: "))
estado = int(input("Ingrese su estado civil (1 = soltero, 2 = casado): "))
if salario <= 10000000:
    print("No debe pagar impuestos sobre su salario anual")
elif salario > 10000000 and salario <= 20000000 and estado == 1:
    impuesto = salario * (10 / 100)
    print("Como soltero, el impuesto a pagar (10%) es:", impuesto, "pesos")
elif salario > 10000000 and salario <= 20000000 and estado == 2:
    impuesto = salario * (5 / 100)
    print("Como casado, el impuesto a pagar (5%) es:", impuesto, "pesos")
elif salario > 20000000 and estado == 1:
    impuesto = salario * (20 / 100)
    print("Como soltero, el impuesto a pagar (20%) es:", impuesto, "pesos")
elif salario > 20000000 and estado == 2:
    impuesto = salario * (15 / 100)
    print("Como casado, el impuesto a pagar (15%) es:", impuesto, "pesos")
else:
    print("Los datos ingresados no son validos")
