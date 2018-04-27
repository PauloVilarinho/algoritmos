num = int(input())

for x in range (1, (num+1)):
	if x%2 != 0 :
		continue
	quadrado = x**2

	print ("%d^2 =" %x, quadrado)