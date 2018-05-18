preco,pagamento = [int(i) for i in input().split()]
notas = [2,5,10,20,50,100]
while preco != 0 or pagamento != 0 :
	troco = pagamento - preco
	possivel = False
	for i in notas:
		if not(possivel):
			for j in notas:
				if ((i + j) == troco ):
					possivel = True
					break
		else :
			break

	if possivel :
		print("possible")
	else :
		print("impossible")
	
	preco,pagamento = [int(i) for i in input().split()]
