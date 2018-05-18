quantity = int(input())

for i in range (quantity):
	lista = input().split()
	n = int(lista[0])
	p = float(lista[1])
	j = int(lista[2])

	q = (1-p)**(n)
	a1 = ((1-p)**(j-1))*p
	if 0<p<1 :
		probabilidade = a1/(1-q)
	elif p==1 and j==1 :
		probabilidade = 1.0000
	else:
		probabilidade = 0.0000
	print("%.4f" %probabilidade)