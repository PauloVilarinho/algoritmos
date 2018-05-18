while True :		
	try:
		volume = float(input())
		diametro = float(input())

		area = 3.14*((diametro/2)**2)
		altura = volume/area

		print("ALTURA = %.2f" %altura)
		print("AREA = %.2f" %area)
	except EOFError :
		break