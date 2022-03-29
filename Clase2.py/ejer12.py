altura =5
espacios=altura
caracteres=1
for i in range(altura):
    for j in range(espacios):
        print("  ",end="")
    for k in range(caracteres):
        print("* ",end="")
    espacios-=1
    caracteres+=2
    print()
