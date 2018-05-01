operation = input()
total = 0
quantity = 0
for i in range (12):
	for j in range (12):
		z = float(input())
		if (i+j)<11 :
			total += z
			quantity += 1
if operation == "S":
	print("%.1f" %total)
if operation == "M":
	print("%.1f" %(total/quantity))