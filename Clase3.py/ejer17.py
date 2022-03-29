saldo =340
op=0
while (op!=3):
    op=int(input("Ingrese opcion:\n1.-Deposito \n2.-Retiro \n3.-Salir \n "))
    if op==1:
        cant=float(input("Ingrese la cantidad: "))
        saldo+=cant
    elif op==2:
        cant=float(input("Ingrese la cantidad: "))
        if saldo>=cant:
            saldo-=cant
        else:
            print ("No tiene saldo disponible")        
    elif op==3:
        print("Saliendoooo")    
    
print ("Saldo Actual es de:  ",saldo)


