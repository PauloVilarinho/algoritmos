quantity = int(input())

entrada = input().split()

montanhoso = True

if int(entrada[0]) > int(entrada[1]) :
	pico = False
elif int(entrada[0]) < int(entrada[1]) :
	pico = True
else :
	montanhoso = False
if montanhoso:
	for i in range(2,quantity) :
		if pico :
			if int(entrada[i]) < int(entrada[i-1]) :
				pico = False
			else :
				montanhoso = False
				break
		else :
			if int(entrada[i]) > int(entrada[i-1]) :
				pico = True
			else :
				montanhoso = False
				break
if montanhoso :
	print(1)
else :
	print(0)