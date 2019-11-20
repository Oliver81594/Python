n = int (input())
a = 1
pole =[0,1]

for i in range(n):
    pole.append(pole[-2] + pole[-1])
    
print(str(pole[0]) , end = '')
    
for i in range (n - 1):
    print(" " + str(pole[a]), end = '')
    a = a + 1
print()
    




