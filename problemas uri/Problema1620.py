valor = int(input())

while valor >0 :
	l = valor+((valor-3))
	x = (l-valor)/valor
	print("%.6f" %x)
	valor = input()
	lista = list(valor)
	if len(lista) >= 3 :	
		if lista[len(lista) - 2] == "e" :
			lista = valor.split("e")
			valor = int(lista[0])**int(lista[1])
		elif lista[len(lista) - 3] == "e" :
			lista = valor.split("e")
			valor = int(lista[0])**int(lista[1])
		else:
			valor = int(valor)
	else :
		valor = int(valor)
