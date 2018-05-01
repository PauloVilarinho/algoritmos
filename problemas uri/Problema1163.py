import math
h = float(input())
p1,p2 = [int(i) for i in input().split()]
quantity = int(input())
g = 9.80665

for i in range(quantity):
	angulo,velocidade = [float(z) for z in input().split()]
	angulo = math.radians(angulo)
	velocidade = velocidade
	velx = velocidade*(math.cos(angulo)) 
	vely = velocidade*(math.sin(angulo))
	delta = vely**2 + 2*g*h
	tempo = ((delta**(1/2))*(-1) - vely)/(-g)
	distancia = tempo*velx
	if p1<distancia<p2:
		print("%.5f -> DUCK" %distancia)
	else:
		print("%.5f -> NUCK" %distancia)