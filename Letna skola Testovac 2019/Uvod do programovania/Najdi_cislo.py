n = int(input())
pole = input().split()

for m in range(n):
	pole[m] = int(pole[m])
	
pocet = int(input())
otazky = []

for i in range(pocet):
	otazky.append(int(input()))

a = 0
b = 0
odpoved = -1


for i in range(pocet):
    for d in range(n):
        if pole[d] == otazky[i]:
            odpoved = d
            break
        
    if odpoved == -1:
        print(-1)
    else:
        print(odpoved)
    odpoved = -1

    
