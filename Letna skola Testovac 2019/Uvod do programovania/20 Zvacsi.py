n = int(input())
pole = []
pole = input().split()

a = 0
b = 0
c = 0



pole2 = []

x = int(input())

for i in range (n):
    pole2.append(int(pole[a]) + x)
    a = a + 1
    

while c <= n:
     if c+1 == n:
        print(pole2[n-1])
        c = c + 2
        
     else:
        print(str(pole2[b]) + " " , end = '')
        b = b + 1
        c = c + 1


