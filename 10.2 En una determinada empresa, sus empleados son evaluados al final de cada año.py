#Ejercicio:En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación, se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400.000 multiplicada por la puntuación del nivel.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
puntuacion = float(input("Ingrese la puntuacion del empleado (0.0, 0.4 o 0.6 o mas): "))
if puntuacion == 0.0:
    nivel = "Inaceptable"
    dinero = 2400000 * puntuacion
    print("Nivel de rendimiento:", nivel, "| Bonificacion a recibir:", dinero, "pesos")
elif puntuacion == 0.4:
    nivel = "Aceptable"
    dinero = 2400000 * puntuacion
    print("Nivel de rendimiento:", nivel, "| Bonificacion a recibir:", dinero, "pesos")
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    dinero = 2400000 * puntuacion
    print("Nivel de rendimiento:", nivel, "| Bonificacion a recibir:", dinero, "pesos")
else:
    print("La puntuacion ingresada no es valida")
