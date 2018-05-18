h1,m1,h2,m2 = [int(i) for i in input().split()]

while h1 != 0 or m1 != 0 or h2 != 0 or m2 != 0 :
	tempoinicial = h1*60 + m1
	tempofinal = h2*60 + m2
	if (tempoinicial>=tempofinal) :
		tempo = 1440 - tempoinicial + tempofinal
	else:
		tempo = tempofinal - tempoinicial
	print(tempo)
	h1,m1,h2,m2 = [int(i) for i in input().split()]	
