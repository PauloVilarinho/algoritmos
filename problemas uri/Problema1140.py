texto = input()
while texto != "*" :
	texto = texto.lower()
	taltogram = True
	vetor_texto = texto.split()
	for i in range(1,len(vetor_texto)):
		if vetor_texto[i][0] != vetor_texto[i-1][0] :
			taltogram = False
			break

	if taltogram :
		print("Y")
	else:
		print("N")

	texto = input()	