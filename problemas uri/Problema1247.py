while True :
	try:
		D, VF, VG = [int(i) for i in input().split()]
		Tempo = 12/VF

		if (VG*Tempo)**2 >= ((D**2)+((VF*Tempo)**2)):
			print("S")
		else:
			print("N")



	except EOFError :
		break