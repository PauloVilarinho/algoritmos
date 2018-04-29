X = int(input())
Y = int(input())
total = 0
if X>= Y:
	for i in range(Y, X+1):
		if (i%13) != 0:
			total = total + i
elif Y> X:
	for i in range(X, Y+1):
		if (i%13) != 0:
			total = total + i

print(total)		
