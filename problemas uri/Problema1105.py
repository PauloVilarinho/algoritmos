bancos,dividas = [int(i) for i in input().split()]

while bancos!=0 or dividas!=0 :
	possivel = True
	dinheiro = [int(i) for i in input().split()]
	for i in range (dividas):
		devedor,credor,quantia = [int(i) for i in input().split()]
		dinheiro[devedor-1] -= quantia
		dinheiro[credor-1] += quantia
	for i in dinheiro:
		if i < 0 :
			possivel = False
			break

	if possivel :
		print("S")
	else :
		print("N")
	bancos,dividas = [int(i) for i in input().split()]

