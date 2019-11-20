n = int(input())
pole = input().split()

for m in range(n):
    pole[m] = int(pole[m])
    
pocet = int(input())
otazky = []

for i in range(pocet):
    otazky.append(int(input()))
    
l = 0
r = n - 1
a = 0
odpoved = -1


for i in range(pocet):
    for z in range(n):
        stred = (l + r)//2
        if pole[stred] == otazky[a]:
            odpoved = stred
            break
        else:
            if pole[stred] < otazky[a]:
                l = stred + 1
            else:
                r = stred - 1
    if odpoved == -1:
        print(-1)
    else:
        print(odpoved)
    odpoved = -1
    l = 0
    r = n - 1
    a = a + 1
