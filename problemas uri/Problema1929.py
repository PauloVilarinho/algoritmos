a,b,c,d = [int(i) for i in input().split()]
lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.sort()
a,b,c,d = [int(i) for i in lista]

if (abs(b - c) < a < b + c) and (abs(a - c) < b < a + c) and (abs(a - b) < c < a + b) :
	print("S")
elif (abs(b - c) < d < b + c) and (abs(d - c) < b < d + c) and (abs(d - b) < c < d + b) :
	print("S")
else :
	print("N")