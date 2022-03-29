jornada = 48
hTrabajada=int(input("horas Trabajadas"))
pagoH=2
pagoE=3.5
print (" ")
if hTrabajada<=jornada:
    salrio = hTrabajada*pagoH
  
else:
    salario =(jornada*pagoH)+((hTrabajada-jornada)*pagoE)

print ("El salario es ",salario)
print (" ")