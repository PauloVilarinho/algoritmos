saidas = 0
numero = 0
while saidas != 3 :
	
	entrada = input()
	if entrada == "caw caw" :
		print(numero)
		numero = 0
		saidas += 1
	else :
		lista = list(entrada)
		lista.reverse()
		for i in range (len(lista)):
			if lista[i] == '*' :
				numero = numero + 2**i
