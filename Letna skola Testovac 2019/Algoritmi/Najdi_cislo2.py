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
odpoved = 0

for i in range(pocet):
	for g in pole:
		if g == otazky[a]:
			odpoved = g
	if odpoved != g:
		print("-1")
	else:
		print(g)
	a = a + 1