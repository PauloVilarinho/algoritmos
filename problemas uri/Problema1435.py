
num = 1
while num != 0 :
	num = int(input())
	y = [0] * (num**2)
	if num%2 == 0:
		quantidade = round(num/2)
	elif num%2 != 0:
		quantidade = round((num+1)/2)

	for k in range (quantidade):
		for i in range (num):
			for j in range (num):
				if ((i == k) or (i == num - (k + 1) ) or (j == k ) or (j == num - (k + 1))) and y[(i*num) + j] == 0 :
					y[(i*num) + j] = k+1

	for i in range (len(y)) :
		if (i+1)%num != 0 :
			print (y[i], end = " ")
		else :
			print(y[i])
	print()
				
						
				