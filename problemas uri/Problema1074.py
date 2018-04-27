quantity = int(input())
tipo = ""
parimpar = ""
for x in range(quantity):
	number = int(input())
	if number>0 :
		tipo = "POSITIVE"
	elif number<0 :
		tipo = "NEGATIVE"
	else :
		tipo = "NULL"

	if (number%2 == 0):
		parimpar = "EVEN"
	elif (number%2 != 0):
		parimpar = "ODD"
	
	if tipo == "NULL":
		print(tipo)
	else:
		print(parimpar, tipo)
