lenth = int(input())
lista = input().split()

for i in range (len(lista)):
	x = int(lista[i]) 
	if i == 0 :
		valor = x
		position = i
	else:
		if x < valor:
			valor = x
			position = i
print("Menor valor: %d" %valor)
print("Posicao: %d" %position)