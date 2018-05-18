a,b,c = [int(i) for i in input().split()]

difer1 = abs(a-b)
difer2 = abs(b-c)

if (a>b and c>=b) :
	feliz = True
elif (a<b and b>=c) :
	feliz = False
elif (a<b<c):
	if difer1>difer2:
		feliz = False
	else :
		feliz = True
elif (a>b>c) :
	if difer1>difer2:
		feliz = True
	else :
		feliz = False
elif a==b :
	if c>b :
		feliz = True
	else :
		feliz = False

if feliz :
	print(":)")
else :
	print(":(")