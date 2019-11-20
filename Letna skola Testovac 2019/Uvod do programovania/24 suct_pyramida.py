n = int(input())

pole = []
pole = input().split()

pole2 =[]
pole3 =[]
pole4 =[]
pole5 =[]
pole6 =[]


a = 0
b = 1
poct_poschodi = n -1

for m in pole: 
    pole2.append(int(m))
    
 
 
 
for i in range (n - 2):
    pole3.append(pole2[a] + pole2[b])
    
print(pole3[0], end = '')


for m in pole3: 
        print(" " + str(m) , end = '')
print() 




for i in range (n - 3):
    pole4.append(pole3[a] + pole3[b])
    
print(pole4[0], end = '')


for m in pole4: 
        print(" " + str(m) , end = '')
print() 




for i in range (n - 4):
    pole5.append(pole4[a] + pole4[b])
    
print(pole5[0], end = '')

for m in pole5: 
        print(" " + str(m) , end = '')
print() 

 
