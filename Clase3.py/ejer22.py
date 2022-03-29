from random import randint


def llenarSec(n):
    lista=[]
    for i in range(1,n+1):
        lista+=[i]
    return lista
def llenarAle(n):
    lista=[]
    num=randint(1,n)
    lista+=[num]
    for i in range(n-1):
        while num in lista:
            num=randint(1,n)
        lista+=[num]
    return lista
print ("GRUPO 1")    
listaA=llenarSec(10)
print (listaA) 
print ("GRUPO 2")  
listaB=llenarAle(10)
print (listaB) 

for i in range(len(listaA)):
    print ("la persona : ",listaA[i],"es pareja con",listaB[i])




