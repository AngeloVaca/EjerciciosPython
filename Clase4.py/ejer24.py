def llenarSecuencia(n):
    tabla=[]
    r=1
    for i in range(n):
      tabla.append([])
      for j in range(n):
          tabla[i]+=[r]
          r+=1
    return tabla

def imprimir (tabla):
   for i in range(len(tabla)):
       print("[",end="")
       for j in range(len(tabla)):
           print("%3s"%tabla[i][j],end="")
       print(" ]")   


tabla =llenarSecuencia(5)
imprimir = imprimir(tabla)
