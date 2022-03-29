lista=["a","b","c","d","e","f","g"]
lista2=["a","e","c","h","i","j","c"]
listaTodo=[]
lSolo1=[]
lSolo2=[]
lAmbas=[]



listaTodo=lista+lista2

for palabra in lista:
    if palabra in lista2:
        lAmbas=lAmbas+[palabra]
    else:
        lSolo1=lSolo1+[palabra]
for palabra in lista2:
    if palabra  not in lista:
        lSolo2=lSolo2+[palabra]

print(lista)
print(lista2)
print(listaTodo)
print(lSolo1)
print(lSolo2)
print(lAmbas)








