while True :		
	try:
		horas,minutos =[int(i) for i in input().split(":") ]

		tempo = horas*60 + minutos

		if tempo > 420 :
			atraso =  tempo - 420
		else : 
			atraso = 0

		print("Atraso maximo:", atraso)
	except EOFError :
		break