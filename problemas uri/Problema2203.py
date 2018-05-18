while True :
	try:
		Xf,Yf,Xi,Yi,Vi,R1,R2 = [int(i) for i in input().split()]

		distancia = (((Xi - Xf)**2) + ((Yi - Yf)**2))**(1/2)
		fuga = 1.5*Vi

		if (distancia+fuga) <= (R1+R2) :
			print("Y")
		else :
			print("N")
	except EOFError :
		break