Coordenadas = input()

X = float(Coordenadas.split()[0])
Y = float(Coordenadas.split()[1])


if (X==0):
	if(Y==0):
		print("Origem")
	else:
		print("Eixo Y")
elif (X>0):
	if (Y>0):
		print("Q1")
	elif(Y<0):
		print("Q4")
	else:
		print("Eixo X")
else:
	if (Y>0):
		print("Q2")
	elif(Y<0):
		print("Q3")
	else:
		print("Eixo X")
