quantity = int(input())

for i in range (quantity):
	x = int(input())
	primo = True
	if (x == 0) or(x == 1) :
			primo = False
	else:		
		for i in range (2,int(x**(1/2))+1):
			if x%i == 0 :
				primo = False
				break

	if primo :
		print("Prime")
	else :
		print("Not Prime")