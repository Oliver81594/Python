stra, strb ,strc ,strd ,stre=input().split()
a, b, c, d, e= int(stra), int(strb), int(strc), int(strd), int(stre)

if a>b and a>c and a>d and a>e:
	print(b+c+d+e)
if b>a and b>c and b>d and b>e:
	print(a+c+d+e)
if c>b and c>a and c>d and c>e:
	print(a+b+d+e)
if d>b and d>c and d>a and d>e:
	print(a+b+c+e)
if e>b and e>c and e>d and e>a:
	print(a+b+c+d)
