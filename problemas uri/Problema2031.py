quantity = int(input())

for i in range (quantity) :
	jogador1 = input()
	jogador2 = input()

	if jogador1 == "ataque" :
		if jogador2 == "ataque" :
			print("Aniquilacao mutua")
		elif jogador2 == "pedra" :
			print("Jogador 1 venceu")
		elif jogador2 == "papel" :
			print("Jogador 1 venceu")
	elif jogador1 == "pedra" :
		if jogador2 == "pedra" :
			print("Sem ganhador")
		elif jogador2 == "papel" :
			print("Jogador 1 venceu")
		elif jogador2 == "ataque" :
			print("Jogador 2 venceu")
	elif jogador1 == "papel" :
		if jogador2 == "papel" :
			print("Ambos venceram")
		elif jogador2 == "pedra" :
			print("Jogador 2 venceu")
		elif jogador2 == "ataque" :
			print("Jogador 2 venceu")