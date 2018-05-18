quantity = int(input())

for i in range (quantity) :
	soldados = int(input())
	auxiliar = 1
	n = 1
	delta = 1+8*soldados
	x1 = (-1 + delta**(1/2))/2
	resposta = int(x1)

	print(resposta)