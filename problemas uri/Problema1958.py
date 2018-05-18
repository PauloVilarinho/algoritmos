numero = float(input())
potencia = 0
lista = list(str(numero))
if numero != 0 :
	while abs(numero)>10 or abs(numero)<1 :
		if abs(numero) <1 :
			numero = numero * 10
			potencia -= 1
		elif abs(numero) > 10 :
			numero = numero/10
			potencia += 1

if numero > 0 :
	textonum = ("+%.4f" %numero)
elif numero == 0 :
	if lista[0] == "-":
		textonum = ("%.4f" %numero)
	else:
		textonum = ("+%.4f" %numero)
else:
	textonum = ("%.4f" %numero)
if 0<=potencia<10 :
	textopot = "+0" +str(potencia)
elif potencia>= 10 :
	textopot = "+" + str(potencia)
elif -10<potencia<0 :
	textopot =  "-0"  +  list(str(potencia))[1]
else :
	textopot = str(potencia)




print("%sE%s" %(textonum,textopot) )