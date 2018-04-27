pares = 0
impares = 0
positivos = 0
negativos = 0
for x in range(5):
	y = float(input())
	if ((y%2)==0) :
		pares = pares + 1
	elif ((y%2)==1) :
		impares = impares + 1

	if (y>0):
		positivos = positivos + 1
	elif (y<0):
		negativos = negativos + 1



print(pares,"valor(es) par(es)")
print(impares,"valor(es) impar(es)")
print(positivos,"valor(es) positivo(s)")
print(negativos,"valor(es) negativo(s)")