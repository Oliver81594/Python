g,h = input().split()
n,x = int(g), int(h)

cisla = input().split()

pole = []
rozdieli = []

odpoved = ""

a = 0
b = 0

for m in cisla:
	pole.append(int(m))
	
for i in range(n*(n-1)):
	if b > n - 1:
		b = 0
		a = a + 1
	rozdieli.append(pole[a] - pole[b])
	b = b + 1

a = 0
b = 0

for i in range(n*(n-1)):
	if a > n - 1:
		a = 0
		b = b + 1
	rozdieli.append(pole[a] - pole[b])
	a = a + 1
	
for s in rozdieli:
	if s == x:
		odpoved = "Ano"
		
if odpoved != "Ano":
	odpoved =  "Nie"
	
print(odpoved)