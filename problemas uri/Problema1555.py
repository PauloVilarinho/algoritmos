quantity = int(input())

for i in range(quantity) :
	x, y = [int(i) for i in input().split()]
	r = 9*(x**2) + y**2
	b = 2*(x**2) + 25*(y**2)
	c = y**3 - (100*x)
	if c > b and c > r :
		print("Carlos ganhou")
	elif b > c and b > r :
		print("Beto ganhou")
	elif r > c and r > b :
		print("Rafael ganhou")