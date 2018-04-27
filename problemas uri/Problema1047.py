ih , im, eh, em = [int(i) for i in input().split()]

tempoinicial= (ih*60) + im
tempofinal= (eh*60) + em

if (eh<ih):
	tempo = 1440 - tempoinicial + tempofinal
elif(eh>ih):
	tempo = tempofinal - tempoinicial
elif(eh == ih):
	if (em>im):
		tempo = em - im
	elif (em<im):
		tempo = 1380 +(60 - im + em)
	elif (em == im):
		tempo = 1440

horas = int(tempo/60)
minutos = int(tempo%60)
	




print ("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(horas,minutos))
