quantity = int(input())

while quantity>0 :
	corridas = 0
	while quantity > 1 :
		if quantity%3 == 0 :
			corridas += quantity//3
			quantity = quantity//3
		else :
			corridas += (quantity//3) + 1 
			quantity = (quantity//3) + 1
	print(corridas)
	quantity = int(input())