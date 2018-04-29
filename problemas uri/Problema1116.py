quantity = int(input())

for i in range (quantity):
	x,y = [int(i) for i in input().split()]
	if y != 0 :
		print("{:.1f}".format(x/y))
	else:
		print("divisao impossivel")