tipo,jogador1,jogador2,roubo1,notou2 = [int(i) for i in input().split()]

total = tipo + jogador2 + jogador1

if total%2 == 0  :
	if roubo1 == 1 and notou2 == 0 :
		print("Jogador 1 ganha!")
	elif roubo1 == 0 and notou2 == 1 :
		print("Jogador 1 ganha!")	
	else :
		print("Jogador 2 ganha!")
else :
	if roubo1 == 1 and notou2 == 1 :
		print("Jogador 2 ganha!")
	else :
		print("Jogador 1 ganha!")