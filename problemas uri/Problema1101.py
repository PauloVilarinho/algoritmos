
bool1 = True
while bool1:
	soma = 0
	texto = ""
	a,b = [ int(i) for i in input().split()]
	if (a<=0) or (b<=0):
		bool1 = False
		break
	if a<=b:
		for i in range (a, b+ 1):
			soma = soma + i 
			texto = texto + str(i) + " "
	if a>b:
		for i in range (b, a+1):
			soma = soma + i 
			texto = texto + str(i) + " "
	print (texto + ("Sum=%d" %soma))


