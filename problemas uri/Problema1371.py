quartos = int(input())

while quartos != 0 :
	i = 1
	while (i**2) <= quartos :
		if ((i**2)+(i+i+1))>quartos :
			print(i**2)
			i = i+1
		else:
			print(i**2, end=" ")
			i = i+1
	quartos = int(input())