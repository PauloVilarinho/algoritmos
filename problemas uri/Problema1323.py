

tamanho = int(input())
while tamanho != 0 :

	total = 0
	for i in range (1, tamanho +1):
		total += i**2

	print(total)
	tamanho = int(input())

