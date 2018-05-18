quantity = int(input())

for i in range (quantity):
	heroi = input().split()[0]
	if heroi == "Thor" :
		print("Y")
	else:
		print("N")