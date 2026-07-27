#Ejercicio:En una plataforma de streaming en Medellín, clasifica a los usuarios en categorías según su historial de consumo. Si han visto más de 100 películas o series, se consideran usuarios premium. Si han visto entre 50 y 100 películas o series, se consideran usuarios estándar. En cualquier otro caso, se consideran usuarios básicos.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
cantidad=int(input("Escriba la cantidad de películas o series vistas: "))
if(cantidad>100):
    print("El usuario es Premium")
elif(cantidad>=50) and (cantidad<=100):
    print("El usuario es Estandar")
else:
    print("El usuario es Basico")
