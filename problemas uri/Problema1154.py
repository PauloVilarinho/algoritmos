x = 1
quantity = 0
total = 0
while x>=0 :
	x = int(input())
	if x>=0:
		total += x
		quantity += 1
print("%.2f" %(total/quantity))