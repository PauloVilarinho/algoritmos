x = []
y = [0]*20
for i in range (20):
	z = int(input())
	x.append(z)
	y[19 - i] = x[i]
for i in range (20):
	print("N[%d] = %d" %(i, y[i]))

