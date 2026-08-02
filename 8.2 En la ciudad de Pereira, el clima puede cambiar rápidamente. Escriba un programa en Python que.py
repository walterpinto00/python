#Ejercicio:En la ciudad de Pereira, el clima puede cambiar rápidamente. Escriba un programa en Python que, dada la variable clima determine qué actividad realizará una persona. Si hace sol, la persona irá al parque. Si está nublado pero no llueve, la persona irá al centro comercial. Si está lloviendo, la persona se quedará en casa.
#Autor:Walter Fabian Pinto Gutierrez
#Fecha:02/08/2026
#Entradas
clima = input("¿Como esta el clima hoy en Pereira? (sol / nublado / lluvia): ").lower()
if clima == "sol":
    print("Hace sol! La persona decidio ir al parque a disfrutar el dia")
elif clima == "nublado":
    print("Esta nublado. La persona decidio ir al centro comercial")
elif clima == "lluvia" or clima == "lloviendo":
    print("Esta lloviendo. La persona decidio quedarse en casa")
else:
    print("No se reconoce ese tipo de clima. Ingrese: sol, nublado o lluvia")
