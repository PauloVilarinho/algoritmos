X = int(input())

def factorial(n):
	total = 1
	while n> 0 :
		total = total*n
		n += -1
	return total
print(factorial(X))
