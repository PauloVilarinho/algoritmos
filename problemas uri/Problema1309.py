while True:
	try:
		reais = list(input())
		centavos = list(input())
		lenth_reais = len(reais)
		lenth_centavos = len(centavos)
		if lenth_centavos == 1 :
			centavos += ["0"]
			centavos.reverse()
		lenth_centavos = len(centavos)
		auxiliar = lenth_reais%3
		print("$", end="")
		for i in range(lenth_reais):
			if auxiliar > 0 :
				auxiliar -= 1
			else:
				auxiliar = 2
			if i == lenth_reais-1 :
				print(reais[i], end=".")
			elif auxiliar == 0 :
				print(reais[i], end=",")
			else:
				print(reais[i], end="")
		for i in range(lenth_centavos):
			if i == lenth_centavos-1 :
				print(centavos[i])
			else:
				print(centavos[i], end="")



	except EOFError :
		break