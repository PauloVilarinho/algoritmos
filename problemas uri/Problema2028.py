caso = 0
while True :		
	try:
		caso += 1
		numero =  int(input())
		sequencia = ["0"]

		for i in range (numero) :
			numero = str(i+1)
			sequencia = sequencia + [numero]*(i+1)
		tamanho  =  len(sequencia)
		if tamanho>1 :
			print("Caso %d: %d numeros" %(caso, tamanho))
		else :
			print("Caso %d: %d numero" %(caso, tamanho))
		print(" ".join(sequencia))
		print()
	except EOFError :
		break