quantity = int(input())

for i in range (quantity) :
	numeros = int(input()) 
	lista = input().split()
	for i in range (len(lista)):
		lista[i] = int(lista[i])
	lista.sort() 
	primo = False
	if lista[0] != 1 :
		maximo = 0
	else:
		for j in range (numeros) :
			if lista[j] != j+1 :
				ultimo = lista[j - 1]
				index = j-1
				break
			index = j
			ultimo = lista[j]
		while not(primo) :
			primo = True	
			ultimo += 1
				ultimo += 2
			if ultimo%2 != 0 :	
				for i in range(3,int((ultimo)**(1/2))+1):
					if ultimo%i == 0 :
						primo = False
						break
			else :
				primo = False
			if primo :
				if (ultimo in lista) :
					primo = False
				else :
					maximo = ultimo - 1
	print(maximo)




