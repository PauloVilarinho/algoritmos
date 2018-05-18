quantity = int(input())

for i in range (quantity) :
	lista = list(input())
	k = 0
	numero = ""
	while lista[len(lista)-1] == "!" :
		lista.pop()
		k += 1
	x = int(numero.join(lista))
	total = 1
	while x > 0 :
		total = total*x
		x = x - k
	print(total)
