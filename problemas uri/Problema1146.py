num = 1
while num != 0 :
	num = int(input())
	for i in range (num):
		if (i+1) != num :
			print(i+1, end = " ")
		else :
			print(i+1)