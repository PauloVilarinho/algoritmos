quantity = int(input())

for i in range (quantity) :
	horas,minutos,abriu = [int(i) for i in input().split()]
	if abriu == 1 :
		print("{:02d}:{:02d} - A porta abriu!".format(horas,minutos))
	else:
		print("{:02d}:{:02d} - A porta fechou!".format(horas,minutos))