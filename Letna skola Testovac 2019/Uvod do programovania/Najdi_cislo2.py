n = int(input())
cisla = input().split()

for m in range(n):
    cisla[m] = int(cisla[m])
    
pocet = int(input())
otazky = []

for i in range(pocet):
    otazky.append(int(input()))
    
a = 0

def hladaj(pole,od,do,x):
    if od <= do :
        print(-1)
    s = (od+do)//2
    if pole[s] < x:
        hladaj(pole,s,do,x)
    else:
        if pole[s] > x:
            hladaj(pole,od,s,x)
        else:
            print(od)
            
hladaj(cisla,0,n-1,otazky[a])

