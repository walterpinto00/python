#Ejercicio:Escribe un programa que pregunte la edad de una persona y determine si es elegible para obtener una licencia de conducir, la licencia se obtiene a partir de los 18 años de edad
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
edad = int(input("Por favor ingrese su edad: "))
if edad >= 18:
    print("Con", edad, "años de edad, SI puede obtener una licencia de conducir")
elif edad > 0:
    print("Con", edad, "años de edad, NO puede obtener una licencia de conducir aun")
else:
    print("La edad ingresada no es valida")
