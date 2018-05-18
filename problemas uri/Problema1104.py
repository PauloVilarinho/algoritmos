cartasalice,cartasbeatriz = [int(i) for i in input().split()]

while cartasbeatriz != 0 or cartasalice != 0 :

	listaalice = input().split()
	listabeatriz = input().split()
	total = 0
	anterior = ""
	if cartasalice > cartasbeatriz :
		for i in range(cartasbeatriz) :
			if not(listabeatriz[i] in listaalice) and listabeatriz[i]!=anterior :
				total += 1
				anterior = listabeatriz[i] 
	else :
		for i in range(cartasalice) :
			if not(listaalice[i] in listabeatriz) and listaalice[i] != anterior :
				total += 1
				anterior = listaalice[i]
	print(total)



	cartasalice, cartasbeatriz = [int(i) for i in input().split()]