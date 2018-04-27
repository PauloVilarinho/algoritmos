coluna = input()
classe = input()
alimento = input()


if (coluna == "vertebrado"):
	if (classe == "ave"):
		if (alimento == "onivoro"):
			print("pomba")
		elif(alimento == "carnivoro"):
			print("aguia")
	elif(classe == "mamifero"):
		if (alimento == "onivoro"):
			print("homem")
		elif(alimento == "herbivoro"):
			print("vaca")
elif (coluna == "invertebrado"):
	if (classe == "inseto"):
		if (alimento == "hematofago"):
			print("pulga")
		elif(alimento == "herbivoro"):
			print("lagarta")
	elif(classe == "anelideo"):
		if (alimento == "onivoro"):
			print("minhoca")
		elif(alimento == "hematofago"):
			print("sanguessuga")