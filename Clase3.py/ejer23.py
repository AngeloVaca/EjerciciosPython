from random import randint


def llenarAle(n):
    lista=[]
    num=randint(60,80)
    lista+=[num]
    for i in range(n-1):
        while num in lista:
            num=randint(60,80)
        lista+=[num]
    return lista

print("PESOS DE LOS SERES HUMANOS")
n=5
lista=llenarAle(n)
print(lista)
mayor=lista[0]
for i in range(n-1):
    for j in range(i+1,n-1):
        if lista[i]!=lista[j]:
             
            suma=lista[i]+lista[j]
            if suma<=150:
                print("el peso de la persona",(i+1),lista[i],"+","persona ",(j+1),lista[j],"es igual a:",suma)

                if suma>mayor:
                    mayor=suma

print("El mayor es de ",mayor)










