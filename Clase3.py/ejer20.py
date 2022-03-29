lista=["Carlos","Carlos","Roberto","Maria","Carlos","ANGELO","ANGELO"]
cont=0;
for i in range((len(lista)-1),-1,-1):
    if lista[i] in lista[:i]:
        del (lista[i])
    
print(lista)            