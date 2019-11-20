a,b,c = input().split()
x,y,z = int(a) , int (b) , int(c)

if x < y:
    if x < z:
        print(x)
    else:
        print(z)
else:
    if y < z:
        print(y)
    else:
        print(z)
