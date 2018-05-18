quantity = int(input())
pair = 0
for i in range(quantity):
	pair += 1
	listaa = list(input())
	listab = list(input())
	listaa.reverse()
	listab.reverse()
	numeroa = 0
	numerob = 0
	for i in range (len(listaa)):
		numeroa += int(listaa[i])*(2**i)
	for i in range (len(listab)):
		numerob += int(listab[i])*(2**i)
	anterior = numeroa
	atual = numerob
	resto = anterior%atual
	while resto != 0:
		anterior = atual
		atual = resto
		resto = anterior%atual
	if atual == 1 :
		print("Pair #%d: Love is not all you need!" %pair)
	else :
		print("Pair #%d: All you need is love!" %pair)
