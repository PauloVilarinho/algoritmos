total = 0
horaa = 0
minutoa = 0
segundoa = 0
velocidade = 0
while True:
	try :	
		lista = input().split()
		
		if len(lista) == 2 :
			horario = lista[0]
			horad,minutod ,segundod = [int(i) for i in horario.split(':')]
			total = total + velocidade*((horad-horaa) + (minutod - minutoa)/60 + (segundod - segundoa)/3600)
			velocidade = int(lista[1])
			horaa = horad
			minutoa = minutod
			segundoa = segundod

		else :
			horario = lista[0]
			horad,minutod,segundod = [int(i) for i in horario.split(':')]
			total += velocidade*((horad-horaa) + (minutod - minutoa)/60 + (segundod - segundoa)/3600)
			horaa = horad
			minutoa = minutod
			segundoa = segundod
			print("%s %.2f km" %(horario,total))	
	except EOFError:
		break