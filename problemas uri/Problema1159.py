x = 1

while x!= 0 :
	total = 0
	x = int(input())
	y = x
	if x%2 == 1:
		x += 1
	if y!= 0 :
		for i in range(5):
			total += x
			x += 2
		print ("%d" %total)

