lista=[1,"hola",3.5,True]


while len(lista)>0:
    print (lista)
    elem=int(input("Ingrese la posicion del elemto a eliminar"))
    if elem>len(lista)-1:
        print ("El Elemento no existe esta fuera de rango")
        continue
    
    del(lista[elem])
    print()
  