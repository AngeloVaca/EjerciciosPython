from random import randint

print()
ganadas=0
ganaM=0
while ganadas < 3 and ganaM<3:
    opUsuario = int (input("Ingrese una opcion:\n1.-Piedra \n2.-Papel \n3.-Tijerra \n4.-respuesta: "))
    opMaquina =randint (1,3)
    print("Usuario escogio",opUsuario)
    print("Maquina escogio",opMaquina)

    if (opUsuario==1 and opMaquina==3) or (opUsuario==2 and opMaquina==1) or (opUsuario==3 and opMaquina==2):
        print("Gana Usuario")
        ganadas+=1
    elif opUsuario== opMaquina:
        print("EMPATE")
    else:
        print("Gana Maquina") 
        ganaM+=1   
    print()

    if ganadas==3:
        print("GANA EL USUARIO EL JUEGO")
    if ganaM==3:
        print("GANA LA MAQUINA EL JUEGO")




