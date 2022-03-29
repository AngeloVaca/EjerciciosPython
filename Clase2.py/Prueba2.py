r="fizz"
s="Buzz"
n=100

for i in range(3,n+1):
    if i%3==0 and i%5==0:
        print(i,r+s)
    elif i%3==0:
        print(i,r)
    elif i%5==0:
        print(i,s)


