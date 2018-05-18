quantity = int(input())

while quantity != 0 :
	for i in range (quantity):
		pessoas = int(input())
		if pessoas%2 == 0 :
			total = (pessoas*2) - 2
		else :
			total = (pessoas*2) - 1
		print(total)
	quantity = int(input())
