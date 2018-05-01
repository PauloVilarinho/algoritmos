X = int(input())
Z = int(input())
while Z <= X:
	Z = int(input())

total = 0
quantity = 0

while total < Z:
	total += X
	X +=1
	quantity += 1

print(quantity)
	