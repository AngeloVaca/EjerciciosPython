correctos = int(input("ingrese el numero de aciertos: "))
errores = int(input("ingrese el numero de errores: "))
total=correctos +errores
promC=(100/total)*correctos
promE=(100/total)*errores
print("Su puntaje final es: "+str(correctos)+"/"+str(total))
print("Su porcentaje de aciertos es: %.2f"%promC,"porcentaje de errores %.2f"%promE)