quantity = int(input())

for i in range (quantity):
	x = int(input())
	total = 0
	for z in range (1,x):
		if x%z == 0 :
			total += z
	if total == x :
		print("%d eh perfeito" % x)
	else:
		print("%d nao eh perfeito" % x)

