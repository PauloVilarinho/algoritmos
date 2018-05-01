quantity = int(input())

for i in range (quantity):
	casas = int(input())
	total = 2**casas - 1 
	peso = int(total/12000)
	print("%d kg" %peso)