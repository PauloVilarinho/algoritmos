while True :
	try:		
		tamanho = int(input())

		for i in range (tamanho) :
			for j in range(tamanho):
				numero = 0
				if i+j == tamanho - 1 :
					numero = 2
				elif i == j :
					numero = 1
				else:
					numero = 3

				if j== tamanho - 1 :
					print("%d" %numero)
				else :
					print("%d" %numero,end="")
	except EOFError :
		break