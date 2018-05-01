quantity = int(input())

for i in range(quantity):
	divisores = 1 
	a,b = [int(z) for z in input().split()]
	anterior = a
	atual = b
	resto = anterior % atual
	while resto != 0:
		anterior = atual
		atual = resto
		resto = anterior % atual
	print(atual)
