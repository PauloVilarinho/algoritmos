
while True:
	try:
		r1,x1,y1,r2,x2,y2 = [int(i) for i in input().split()]

		distancia = ((x1-x2)**2 + (y1 - y2)**2)**(1/2)
		if distancia+r2<=r1 :
			print("RICO")
		else:
			print("MORTO")
	    
	except EOFError:
		break
