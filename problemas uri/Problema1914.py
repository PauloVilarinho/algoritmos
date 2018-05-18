quantity = int(input())

for i in range (quantity):
	jogador1,tipo1,jogador2,tipo2 = [i for i in input().split()]
	numero1,numero2 = [int(i) for i in input().split()]
	total = numero2 + numero1
	if total%2 == 0 :
		ganhador = "PAR"
	else:
		ganhador = "IMPAR"

	if tipo1 == ganhador :
		print(jogador1)
	elif tipo2 == ganhador :
		print(jogador2)