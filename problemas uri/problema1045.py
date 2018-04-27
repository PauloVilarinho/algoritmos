a,b,c = [float(i) for i in input().split()]
lista = [a,b,c]

lista.sort( reverse = True )

a = lista[0]
b = lista[1]
c = lista[2]

if (a>=b+c):
	print("NAO FORMA TRIANGULO")
elif(a**2 == (b**2)+(c**2)):
	print("TRIANGULO RETANGULO")
	if(a == b != c or a != b == c or a == c != b):
		print("TRIANGULO ISOSCELES")
elif(a**2 > (b**2)+(c**2)):
	print("TRIANGULO OBTUSANGULO")
	if((a == b and b != c) or (a != b and b == c) or (a == c and c != b)):
		print("TRIANGULO ISOSCELES")
	elif (a == b == c):
		print("TRIANGULO EQUILATERO")
elif(a**2 < (b**2)+(c**2)):
	print("TRIANGULO ACUTANGULO")
	if((a == b and b != c) or (a != b and b == c) or (a == c and c != b)):
		print("TRIANGULO ISOSCELES")
	elif (a == b == c):
		print("TRIANGULO EQUILATERO")