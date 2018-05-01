colum = int(input())
operation = input()
total = 0
for i in range (144):
	z = float(input())
	if i%12 == colum:
		total += z
if operation == "S":
	print("%.1f" %total)
if operation == "M":
	print("%.1f" %(total/12))