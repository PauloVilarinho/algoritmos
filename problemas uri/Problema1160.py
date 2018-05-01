import math
quantity = int(input())

for i in range (quantity):
	lista = input().split()
	pa = int(lista[0])
	pb = int(lista[1])
	ga = float(lista[2])
	gb = float(lista[3])
	years = 0
	while pa<=pb and years<= 100:
		pa = math.floor(pa*((100+ga)/100))
		pb = math.floor(pb*((100+gb)/100))
		years += 1
	if years <= 100:
		print("%d anos." %years)
	else:
		print("Mais de 1 seculo.")