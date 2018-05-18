while True :
	try:	
		mes,dia = [int(i) for i in input().split()]

		if mes == 12 :
			if (dia < 24) :
				print("Faltam %d dias para o natal!" %(25 - dia))
			elif dia == 24 :
				print("E vespera de natal!")
			elif dia == 25 :
				print("E natal!")
			else:
				print("Ja passou!")
		elif mes == 11 :
			print("Faltam %d dias para o natal!" %(55-dia))
		elif mes == 10 :
			print("Faltam %d dias para o natal!" %(86-dia))
		elif mes == 9 :
			print("Faltam %d dias para o natal!" %(116-dia))
		elif mes == 8 :
			print("Faltam %d dias para o natal!" %(147-dia))
		elif mes == 7 :
			print("Faltam %d dias para o natal!" %(178-dia))
		elif mes == 6 :
			print("Faltam %d dias para o natal!" %(208-dia))
		elif mes == 5 :
			print("Faltam %d dias para o natal!" %(239-dia))
		elif mes == 4 :
			print("Faltam %d dias para o natal!" %(269-dia))
		elif mes == 3 :
			print("Faltam %d dias para o natal!" %(300-dia))
		elif mes == 2 :
			print("Faltam %d dias para o natal!" %(329-dia))
		elif mes == 1 :
			print("Faltam %d dias para o natal!" %(360-dia))	
	except EOFError :
		break
