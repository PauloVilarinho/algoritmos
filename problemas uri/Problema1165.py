quantity = int(input())

for i in range (quantity):
	x = int(input())
	total = 0
	for z in range (1,x):
		if x%z == 0 :
			total += z
	if total == 1 :
		print("%d eh primo" % x)
	else:
		print("%d nao eh primo" % x)

