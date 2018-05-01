def factorial(n):
	total = 1
	while n> 0 :
		total = total*n
		n += -1
	return total

while True:
	try:
		a,b = [int(i) for i in input().split()]
		total = factorial(a)+factorial(b)
		print(total)
	except EOFError:
		break