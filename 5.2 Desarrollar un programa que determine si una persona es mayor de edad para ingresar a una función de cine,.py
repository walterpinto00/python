#Ejercicio:Desarrollar un programa que determine si una persona es mayor de edad para ingresar a una función de cine, y en caso contrario, le informe que necesita la compañía de un adulto
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
edad = int(input("Ingrese la edad de la persona: "))
if edad >= 18:
    print("La persona tiene", edad, "años. Puede ingresar al cine sin problema")
elif edad > 0 and edad < 18:
    print("La persona tiene", edad, "años. Debe ingresar acompañada de un adulto")
else:
    print("La edad ingresada no es valida")
