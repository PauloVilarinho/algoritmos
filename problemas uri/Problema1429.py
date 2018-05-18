numero = list(input())
while not(len(numero) == 1  and numero[0] == "0") :
	total = 0
	factorial = [0 , 1 , 2 , 6 , 24 , 120 ]
	numero.reverse()
	for i in range (len(numero)):
		total += int(numero[i])*factorial[i+1]

	print(total)
	numero = list(input())
