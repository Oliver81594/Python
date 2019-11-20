g,h = input().split()
n,x = int(g), int(h)

f = []
f = input().split()

odpoved = ""

pole = []
rozdieli = []

a = 0
b = 1

for m in f: 
    pole.append(int(m))
    

for i in range(n):
    rozdieli.append(int(pole[a]) - int(pole[b]))
    a = a + 1

a = 0
    
for i in range(n):
    rozdieli.append(int(pole[b]) - int(pole[a]))
    b = b + 1
    
b = 0


for m in rozdieli:
    if m == x:
        odpoved = "Ano"
        
if odpoved != "Ano":
    odpoved = "Nie"
    
print(odpoved)
