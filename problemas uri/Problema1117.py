bool1 = True
notas = 0
total = 0
while bool1 :
	a = float(input())
	if  0 <= a <= 10 :
		total = total + a
		notas = notas + 1
		if notas == 2 :
			bool1 = False
			print("media = {:.2f}".format(total/2))
	else: 
		print("nota invalida")
