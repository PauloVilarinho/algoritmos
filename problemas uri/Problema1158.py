quantity = int(input())

for i in range(quantity):
	total = 0
	x,y = [int(i) for i in input().split()]
	if x%2 == 0:
		x += 1
	for z in range(y):
		total += x
		x += 2
	print(total)
