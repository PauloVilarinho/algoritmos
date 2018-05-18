valor = int(input())

vetor = [0,1/6]
i = 1
while len(vetor)<110 :
	numero = 1/(6+ vetor[i])
	vetor.append(numero)
	i += 1

total = 3 + vetor[valor]
print("%.10f" %total)
