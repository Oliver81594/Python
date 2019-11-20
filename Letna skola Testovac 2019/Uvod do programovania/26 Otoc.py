x = int(input())

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
b = len(stvorec1) - 1
	
for i in range(x*x + 1):
	if a > 2:
		b = b - 1
		a = 0
		stvorec2.append(riadok)
		riadok = []
	riadok.append(stvorec1[a][b])
	a = a + 1
	
a = 0 
print(stvorec2)	
#for i in range(x):
#	print(stvorec2[a])
#	a = a + 1
	
