#Ejercicio:En una plataforma de streaming en Medellín, clasifica a los usuarios en categorías según su historial de consumo. Si han visto más de 100 películas o series, se consideran usuarios premium. Si han visto entre 50 y 100 películas o series, se consideran usuarios estándar. En cualquier otro caso, se consideran usuarios básicos.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
cantidad = int(input("Ingrese la cantidad de peliculas o series vistas por el usuario: "))
if cantidad > 100:
    categoria = "PREMIUM"
    print("El usuario ha visto", cantidad, "contenidos. Categoria asignada:", categoria)
elif cantidad >= 50 and cantidad <= 100:
    categoria = "ESTANDAR"
    print("El usuario ha visto", cantidad, "contenidos. Categoria asignada:", categoria)
elif cantidad >= 0:
    categoria = "BASICO"
    print("El usuario ha visto", cantidad, "contenidos. Categoria asignada:", categoria)
else:
    print("La cantidad ingresada no es valida")
