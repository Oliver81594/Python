n = int(input())
pole = input().split()

for m in range(n):
    pole[m] = int(pole[-m])
    
pocet = int(input())
otazky = []

for i in range(pocet):
    otazky.append(int(input()))
    
print(pole)
