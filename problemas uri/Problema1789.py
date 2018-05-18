while True:			
	try:
		quantity = int(input())

		maximo = 0
		lista = input().split()
		for i in range (quantity) :
			x = int(lista[i])
			if (x > maximo) :
				maximo = x

		if (maximo < 10) :
			print(1)
		elif (10<=maximo<20) :
			print(2)
		elif (maximo>=20) :
			print(3)
	except EOFError :
		break