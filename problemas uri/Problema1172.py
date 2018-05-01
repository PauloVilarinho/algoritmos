x = [0,0,0,0,0,0,0,0,0,0]
for i in range (10):
	z = int(input())
	if z>0:
		x[i] = z
	else:
		x[i] = 1
	print ( "X[%d] = %d" %(i,x[i]) )