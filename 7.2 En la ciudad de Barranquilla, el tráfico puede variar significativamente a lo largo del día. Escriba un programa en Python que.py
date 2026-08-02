#Ejercicio:En la ciudad de Barranquilla, el tráfico puede variar significativamente a lo largo del día. Escriba un programa en Python que, dada la hora del día, determine el nivel de tráfico. Si la hora está entre 6 y 9 (hora pico mañana), el tráfico es alto. Si está entre 12 y 14 (hora pico mediodía), el tráfico es moderado. Si está entre 17 y 19 (hora pico tarde), el tráfico es alto. En cualquier otro caso, el tráfico es bajo.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
hora = int(input("Ingrese la hora del dia (0-23): "))
if hora >= 6 and hora <= 9:
    print("Nivel de trafico a las", hora, "horas: ALTO (hora pico de la manana)")
elif hora >= 12 and hora <= 14:
    print("Nivel de trafico a las", hora, "horas: MODERADO (hora pico del mediodia)")
elif hora >= 17 and hora <= 19:
    print("Nivel de trafico a las", hora, "horas: ALTO (hora pico de la tarde)")
elif hora >= 0 and hora <= 23:
    print("Nivel de trafico a las", hora, "horas: BAJO")
else:
    print("La hora ingresada no es valida (debe ser entre 0 y 23)")
