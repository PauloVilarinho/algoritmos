a = int(input())
b = int(input())
total = 0
if a>b :
	for x in range (b,a):
		if x%2 == 0 :
			continue
		elif x == b	:
			continue
		total = total + x
elif a<b :
	for x in range (a,b):
		if x%2 == 0 :
			continue
		elif x == a :
			continue	
		total = total + x
print (total)