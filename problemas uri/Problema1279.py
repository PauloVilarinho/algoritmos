i = 0
while True :
	try:
		if i != 0 :
			print()

		ano = int(input())

		bisexto = False
		huluculu = False
		bulukulu = False

		if (ano%4 == 0) and (ano%100 != 0) :
			bisexto = True
			if ano%55 == 0:
				bulukulu = True
		elif ano%400 == 0 :
			bisexto = True
			if ano%55 == 0:
				bulukulu = True
		if (ano%15 == 0) :
			huluculu = True

		if bisexto :
			print("This is leap year.")
			if huluculu :
				print("This is huluculu festival.")	 
			if bulukulu :
				print("This is bulukulu festival year.")
		elif huluculu :
			print("This is huluculu festival.")	
		else:
			print("This is an ordinary year.") 
		i += 1
	except EOFError :
		break