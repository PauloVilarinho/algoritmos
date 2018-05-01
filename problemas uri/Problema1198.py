while True:
	try:
		a,b = [int(i) for i in input().split()]
		maior = (a+b+abs(a-b))/2
		menor = (a+b-abs(a-b))/2
		print(int(maior	- menor))
	except EOFError :
		break