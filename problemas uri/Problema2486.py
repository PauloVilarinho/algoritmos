cardapio = {"suco de laranja":120,"morango fresco":85,"mamao":85,"goiaba vermelha":70, "manga":56, "laranja":50, "brocolis":34}

quantity = int(input())

while quantity != 0:
	vitc = 0	
	for i in range (quantity) :
		alimento = ""
		texto = input()
		number = int(texto.split()[0])
		for i in range(1,len(texto.split())):
			if i != (len(texto.split()) -1) :
				alimento += texto.split()[i] + " "
			else :
				alimento += texto.split()[i]
		vitc += number*cardapio[alimento]

	if vitc < 110 :	
		aux = 110 - vitc
		print("Mais {} mg".format(aux))
	elif vitc <= 130:
		print("{} mg".format(vitc))
	else :
		aux = vitc - 130
		print("Menos {} mg".format(aux)) 
	


	quantity = int(input())	