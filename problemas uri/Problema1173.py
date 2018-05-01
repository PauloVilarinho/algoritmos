x = []
z = int(input())
for i in range (10):
	x.append(z)
	z = z*2
	print ("N[%d] = %d" %(i,x[i]))