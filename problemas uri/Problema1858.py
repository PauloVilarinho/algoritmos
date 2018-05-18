x = int(input())

lista = input().split()
minimo = 101
for i in range (x) :
	if int(lista[i]) < minimo :
		minimo = int(lista[i])
		index = i + 1
print(index)