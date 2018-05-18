texto = "LIFE IS NOT A PROBLEM TO BE SOLVED"
lista = list(texto)
quantidade = int(input())
soma = 0
for i in range (quantidade):
	if i == quantidade -1 :
		print(lista[i])
	else:
		print(lista[i], end = "")