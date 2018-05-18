idade = int(input("qual é a idade do seu filho? "))
sexo = input("qual o sexo do seu filho? (M ou H)")

if idade>15 :
	print("seu filho nao tomará nenhuma vacina.")
elif sexo == "H" :
	if idade<11 :
		print("seu filho tomará somente a vacina da gripe")
	elif idade<=12 :
		print("seu filho tomará a vacina da gripe e do HPV")
	elif idade<=13 :
		print("seu filho tomará somente a vacina da HPV")
	else :
		print("seu filho nao tomará nenhuma vacina.")
elif sexo == "M" :
	if idade<9 :
		print("sua filha tomará somente a vacina da gripe")
	elif idade<=12 :
		print("sua filha tomará a vacina da gripe e do HPV")
	elif idade<=15 :
		print("sua filha tomará somente a vacina da HPV")
	else :
		print("sua filha nao tomará nenhuma vacina.")

 
