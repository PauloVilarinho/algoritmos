quantity = int(input())

for i in range (quantity):
	numero1, numero2 = [i for i in input().split()]
	vetor1 = list(numero1)
	vetor2 = list(numero2)
	vetor1.reverse()
	vetor2.reverse()
	encaixa = True
	if len(vetor1)>= len(vetor2) :
		for j in range(len(vetor2)):
			if vetor2[j] != vetor1[j]:
				encaixa = False
	else:
		encaixa = False
	if encaixa :
		print("encaixa")
	else:
		print("nao encaixa")