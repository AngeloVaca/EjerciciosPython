frase="sahdasjdjcjada ahdgasj hasdgaj"
letra="u"
cont=0

for caracter in frase:
    if caracter==letra:
        cont+=1
if cont>0:
 print("La letra se encontro: "+str(cont)+" veces en la frase" )
else:
    print("La letra no se encontro en la frase ")