anioInicio=2000
anioFin=2120
r="Los años bisiestos entre"+str(anioInicio)+" y "+str(anioFin)+" son: "
for i in range(anioInicio,anioFin):
    if(i%4==0 and i%100!=0)or i%400==0:
        r+=str(i)+","
print(r)