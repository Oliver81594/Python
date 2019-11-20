n = int(input())
cisla = input().split()
pole = []

for m in cisla:
	pole.append(int(m))
	
pocet = int(input())
otazky = []

for i in range(pocet):
	otazky.append(int(input()))

a = 0
b = 0
odpoved = 0

for i in range(pocet):
	for i in range(len(pole)):
		if pole[b] == otazky[a]:
			odpoved = b
			b = b + 1
	if odpoved != b:
		print("-1")
	else:
		print(b)
	a = a + 1
	
	odpoved = 0