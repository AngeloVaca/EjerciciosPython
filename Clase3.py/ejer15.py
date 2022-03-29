


def vasos(n,x):
    total=0
    while n>=x:
        reciclados = n//x
        sobran = n%x
        total+=reciclados        
        n=reciclados + sobran
        print("n= ",n,"Reciclados: ",reciclados,"sobran: ",sobran,"total",total)
    return total     

n=68
x=8
vasos(n,x)


        
   
    



        