#Ejercicio:En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación, se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400.000 multiplicada por la puntuación del nivel.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
puntuacion = float(input("Ingrese la puntuación (0.0, 0.4 o 0.6 o más): "))
if(puntuacion==0.0):
    nivel="Inaceptable"
    dinero=2400000*puntuacion
    print("Nivel de rendimiento:",nivel" y el dinero a recibir es:",dinero)
elif(puntuacion==0.4):
    nivel="Aceptable"
    dinero=2400000*puntuacion
    print("Nivel de rendimiento:",nivel" y el dinero a recibir es:",dinero)
elif(puntuacion>=0.6):
    nivel="Meritorio"
    dinero=2400000*puntuacion
    print("Nivel de rendimiento:",nivel" y el dinero a recibir es:",dinero)
else:
    print("Error")


