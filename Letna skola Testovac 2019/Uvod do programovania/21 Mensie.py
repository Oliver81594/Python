n = int(input())
pole = []
sucet = 0

pole = input().split()

x = int(input())

a = 0 

for i in range (n):
    if int(pole[a]) < x:
        sucet = sucet + int(pole[a])
    a = a + 1
print(sucet)
    
    
