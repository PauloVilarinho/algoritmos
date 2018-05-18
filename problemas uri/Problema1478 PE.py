num = 1
x = 0
while num != 0 :
	num = int(input())
	for i in range(1,num +1):
		x = i
		if i == 1 :
			caindo = False
		else :
			caindo = True
		for j in range(1,num +1):
			if j != num :
				print("{:>3}".format(x), end = " ")
			else :
				print("{:>3}".format(x))
			if x == 1:
				caindo = False
			if caindo :
				x += -1
			else:
				x +=1
	print()
		


