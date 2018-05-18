quantity = int(input())
alternativas = {0:"A" , 1:"B" , 2:"C" , 3:"D" , 4:"E"}
while quantity!= 0 :
	for i in range(quantity) :
		respondido = False
		respostas = [int(j) for j in input().split()]
		for k in range(len(respostas)):
			if respostas[k] <= 127 :
				if not(respondido):
					alternativa = k
					respondido = True
				else :
					respondido = False
					break
		if respondido :
			print(alternativas[alternativa])
		else :
			print("*")
	quantity = int(input())

