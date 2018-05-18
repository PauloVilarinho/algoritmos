quantity = int(input())
for i in range (quantity):
	x = input().split()
	lenth = len(x)
	total = 0
	acimadamedia = 0
	for i in range (1,lenth):
		total += int(x[i])
	media = total/(lenth-1)
	for i in range (1,lenth):
		if int(x[i]) > media :
			acimadamedia += 1
	percetagem = (acimadamedia/(lenth-1))*100

	print("{:.3f}%".format(percetagem))