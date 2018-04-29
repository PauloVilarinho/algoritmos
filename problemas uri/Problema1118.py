cal = 1

while cal == 1 :
	X = float(input())
	while 0>X or X>10 :
		print ("nota invalida")
		X = float(input())
	Y = float(input())
	while 0>Y or Y>10 :
		print ("nota invalida")
		Y = float(input())
	med  = (Y+X)/2
	print("media = %.2f" %med)
	cal = int(input("novo calculo (1-sim 2-nao)\n"))
	while (cal > 1 and cal !=2) or cal < 1:
		cal = int(input("novo calculo (1-sim 2-nao)\n"))
