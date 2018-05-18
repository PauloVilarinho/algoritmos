sitios = int(input())
carneiros = input()
i = 0
maximo = 0
roubados = 0
subindo = True
valor = []
while 0<=i<sitios :
	if subindo:
		valor.append(int(carneiros.split()[i]))
	if i > maximo :
		maximo = i
	if valor[i] > 0 :
		roubados +=1
		valor[i] -=1
		if (valor[i]%2 == 0) :
			i += 1
		else :
			i -= 1
			subindo = False	
	else :
			i -= 1
			subindo = False


	
total = 0
for i in range(sitios) :
	total += int(carneiros.split()[i])
total  = total - roubados
	
print(maximo+1,total)