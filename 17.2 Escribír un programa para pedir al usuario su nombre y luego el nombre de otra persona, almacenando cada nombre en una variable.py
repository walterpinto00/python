#Ejercicio:Escribír un programa para pedir al usuario su nombre y luego el nombre de otra persona, almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que indique si: los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Por ejemplo, si los nombres ingresados son María y Marcos, se mostrará True, ya que ambos comienzan con la misma letra. Si los nombres son Ricardo y Gonzalo se mostrará True, ya que ambos terminan con la misma letra. Si los nombres son Florencia y Lautaro se mostrará False, ya que no coinciden ni la primera ni la última letra.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
nombre1 = input("Ingrese su nombre: ")
nombre2 = input("Ingrese el nombre de otra persona: ")
print("Comparando:", nombre1, "y", nombre2)
if nombre1[0].lower() == nombre2[0].lower():
    print("Ambos nombres comienzan con la misma letra:", True)
elif nombre1[-1].lower() == nombre2[-1].lower():
    print("Ambos nombres terminan con la misma letra:", True)
else:
    print("Los nombres no comparten ni la primera ni la ultima letra:", False)
