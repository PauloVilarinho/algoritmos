while True :
	try:	
		a,b,c = [int(i) for i in input().split()]
		lista = [a,b,c]
		lista.sort()
		a = lista[0]
		b = lista[1]
		c = lista[2]
		pitagorica = False
		primitiva = True
		if (c**2) == (b**2) + (a**2) :
			pitagorica = True
			if a>2 :
				for i in range (2,a):
					if a%i == 0 and b%i == 0 and c%i == 0 :
						primitiva = False
						break
			else :
				primitiva = True
		if pitagorica :
			if primitiva:
				print("tripla pitagorica primitiva")
			else:
				print("tripla pitagorica")
		else:
			print("tripla")
	except EOFError :
		break