x,y,z,o,q = input().split()
a,b,c,d,e = int(x), int (y), int (z), int (o), int (q)

if a<b and a<c and a<d and a<e :
print(b+c+d+e)

if b<a and b<c and b<d and b<e :
print(a+c+d+e)

if c<b and c<a and c<d and c<e :
print(b+a+d+e)

if d<b and d<c and d<a and d<e :
print(b+c+a+e)

if e<b and e<c and e<d and e<a :
print(b+c+d+a)
