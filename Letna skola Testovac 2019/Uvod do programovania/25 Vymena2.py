g,h = input().split()
x,y = int(g), int(h)

riadok = []
stvorec1 = []
stvorec2 = []

a = 0
b = 0

for i in range(x):
	riadok = input().split()
	stvorec1.append(riadok)
	riadok = []
	
a = 0
b = y - 1
	
for i in range(x*y + 1):
	if a > x - 1:
		b = b - 1
		a = 0
		stvorec2.append(riadok)
		riadok = []
	riadok.append(stvorec1[a][b])
	a = a + 1
	
a = y - 1
b = 0
for i in range(x*y):
    if b == x - 1:
        print(stvorec2[a][b], end = '')
        b = 0
        a = a - 1
        print()
    else:
        print(stvorec2[a][b] + " ", end = '')
        b += 1


