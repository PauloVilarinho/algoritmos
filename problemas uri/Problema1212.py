a ,b = [i for i in input().split()]

while a!= "0" or b != "0" :
	al = list(a)
	bl = list(b)
	av = [0]*10
	bv = [0]*10
	bl.reverse()
	al.reverse()
	carrys = 0
	for i in range(len(al)):
		av[i] = int(al[i])
	for i in range(len(bl)):
		bv[i] = int(bl[i])
	for i in range(len(av)-1):
		c = av[i]+bv[i]
		if c>=10 :
			bv[i+1] += 1
			carrys += 1
	if carrys == 1 :
		print("1 carry operation.")
	elif carrys == 0 :
		print("No carry operation.")
	elif carrys>0 :
		print("%d carry operations." %carrys)

	a ,b = [i for i in input().split()]

