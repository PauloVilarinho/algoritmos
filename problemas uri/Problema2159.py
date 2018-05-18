import math
numero = int(input())
minimo = numero/math.log(numero)
maximo = minimo*1.25506

print("{:.1f} {:.1f}".format(minimo,maximo))