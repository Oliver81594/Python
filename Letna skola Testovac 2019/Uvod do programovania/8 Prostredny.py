a,b,c = input().split()
x,y,z = int(a) , int (b) , int(c)

if a<b<c or c<b<a:
    print(b)
if a<c<b or b<c<a:
    print(c)
if b<a<c or c<a<b:
    print(a)
