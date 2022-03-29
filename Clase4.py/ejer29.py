def Imprimir (dic):
    for indice in dic:
        print("Producto: ",indice,"Precio: ",dic[indice])



dic= {}
dic["pan"]=.12
total=0   
menu =True
while menu:
    op=int(input("Elija una opcion \n1.-Agregar Producto \n2.-Facturar\n3.-Salir\n"))
    if op ==1:
        indice =input("Ingrese el indice: ")
        valor =float(input("Elija una valor: "))
        dic[indice]=valor
        print (dic)
        
    elif op ==2:
          
        factura=True
        while factura:
            Imprimir(dic)
            of=int(input("Elija una opcion \n1.-Agregar a Factura \n2.-Salir\n"))
            if of ==1:
                indice =input("Ingrese el indice: ")
                cantidad =int(input("Elija una valor: "))
                total +=float(dic.get(indice))*cantidad
                print ("El total es : ",total)
            else:
                factura=False
                total=0     

    elif op ==3:
        menu = False    
    else:
        print("Ingrese una opcion valida: ")





