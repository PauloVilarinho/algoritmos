bool1 = True
while bool1 :
	a,b = [ int(i) for i in input().split()]
	if a > b :
		print("Decrescente")
	elif a < b :
		print("Crescente")
	elif a == b :
		bool1 = False
