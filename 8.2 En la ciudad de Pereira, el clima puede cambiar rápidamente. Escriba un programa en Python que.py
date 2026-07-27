#Ejercicio:En la ciudad de Pereira, el clima puede cambiar rápidamente. Escriba un programa en Python que, dada la variable clima determine qué actividad realizará una persona. Si hace sol, la persona irá al parque. Si está nublado pero no llueve, la persona irá al centro comercial. Si está lloviendo, la persona se quedará en casa.
#Autor:Stiven Aparicio Vega
#Fecha:25/09/2025
#Entradas
clima=input("¿Como esta el clima?(sol, nublado, lluvia): ")
if(clima=="sol"):
    print("La persona ira al parque")
elif(clima=="nublado"):
    print("La persona ira al centro comercial")
elif(clima == "lluvia") or (clima=="lloviendo"):
    print("La persona se quedara en la casa")
else:
    print("Error")
