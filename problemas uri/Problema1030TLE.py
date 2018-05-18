quantity = int(input())
caso = 0
for i in range (quantity):
	caso += 1
	persons, steps = [int(j) for j in input().split()]
	vivos = [True]*persons
	mortos = 0
	aux = 0
	j = 0
	while mortos<(persons-1) :
		if vivos[j]:
			aux +=1
			if aux == steps :
				vivos[j] = False
				mortos += 1
				aux = 0
		if j<(persons-1) :
			j += 1
		else :
			j = 0
	index = vivos.index(True)
	print(index+1)

