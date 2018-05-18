quantity =  int(input())

for i in range (quantity) :
	nome = input()
	dificuldade = float(input())
	notas = [float(i) for i in input().split()]
	notas.sort()
	tamanho = len(notas)
	total = 0
	for i in range(1,tamanho-1) :
		total += notas[i]
	resultado = total*dificuldade
	print("%s %.2f" %(nome,resultado))

	
