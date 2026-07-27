#Ejercicio:Escribír un programa para pedir al usuario su nombre y luego el nombre de otra persona, almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que indique si: los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Por ejemplo, si los nombres ingresados son María y Marcos, se mostrará True, ya que ambos comienzan con la misma letra. Si los nombres son Ricardo y Gonzalo se mostrará True, ya que ambos terminan con la misma letra. Si los nombres son Florencia y Lautaro se mostrará False, ya que no coinciden ni la primera ni la última letra.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
nombre1=input("Escriba el primer nombre: ")
nombre2=input("Escriba el segundo nombre: ")
if(nombre1[0]==nombre2[0]):
    print(True)
elif(nombre1[-1]==nombre2[-1]):
    print(True)
else:
    print(False)
