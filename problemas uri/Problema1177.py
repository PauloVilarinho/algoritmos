x = int(input())
y = []
z = 0
while len(y) <1000 :
	y.append(z)
	if z < x - 1 :
		z += 1
	elif z >= (x-1):
		z = 0

for i in range (len(y)):
	print("N[%d] = %d" %(i,y[i]))