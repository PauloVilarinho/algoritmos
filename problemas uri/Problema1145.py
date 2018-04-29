a,b = [int(i) for i in input().split()]

num = 0 
while num != b :
	num += 1
	if num%a != 0 :
		print(num, end = " ")
	else:
		print(num)