x=input()
pole=input().split()
a=int(x)
b=a
for i in range(a):
	pole[i] = int(pole[i])
for m in range(a-1):
	b-=1
	for n in range(b):
		pole[n]=pole[n]+pole[n+1]
		
		print(pole[n],end=' ')
		
	print()
			
		
