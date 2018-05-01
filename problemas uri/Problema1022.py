quantity = int(input())

for i in range (quantity):
	text = input().split()
	n1 = int(text[0])
	d1 = int(text[2])
	n2 = int(text[4])
	d2 = int(text[6])
	operation = text[3]
	divisores = 1

	if operation == "+" :
		cima = (n1*d2 + n2*d1)
		baixo = d1*d2
	elif operation == "-" :
		cima = (n1*d2 - n2*d1)
		baixo = d1*d2
	elif operation == "*" :
		cima = n1*n2
		baixo = d1*d2
	elif operation == "/" :
		cima = n1*d2
		baixo = n2*d1
	cimad = cima
	baixod = baixo

	for j in range (2,baixo):
		while cimad%j == 0 and baixod%j == 0 :
			cimad = cimad/j
			baixod = baixod/j

	print("%d/%d = %d/%d" %(cima,baixo,cimad,baixod))

