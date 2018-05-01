quantity = int(input())
total = 10

for i in range (quantity):
	total = float(input())
	dias = 0
	while total>1 :
		total = total/2
		dias += 1
	print("%d dias" %dias)
	