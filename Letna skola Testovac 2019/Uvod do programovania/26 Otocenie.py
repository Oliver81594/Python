x = int(input())
a = 0
b = 0

stvorec1 = []
stvorec2 = [] 
riadok = []

for i in range (x):
    riadok.append(input().split())
    stvorec1.append(riadok)
    riadok = []



def otocenie():
    if x+1 == a:
        a = 0
    else:
        if b == x+1:
            stvorec2.append(riadok)
            b = 0
            a = a + 1
            riadok = []
        else:
            riadok.append(stvorec1[b][a])
            b = b + 1
        
for i in range (x):
    otocenie()


print(stvorec2)


    
