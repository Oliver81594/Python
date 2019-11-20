palindrom = input()

a = 0
b = -1
odpoved = ""

x = int(len(palindrom))
y = x / 2

for i in range (x):
    if palindrom[a] != palindrom[b]:
        odpoved = "nepali"
    a = a + 1
    b = b - 1
    
if odpoved != "nepali":
    odpoved = "pali"
    
print(odpoved)
