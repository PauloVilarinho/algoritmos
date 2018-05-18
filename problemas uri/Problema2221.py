quantity = int(input())

for i in range (quantity) :
	bonus = int(input())
	ataque1,defesa1,level1 = [int(i) for i in input().split()]
	ataque2,defesa2,level2 = [int(i) for i in input().split()]
	valor1 = ((ataque1+defesa1)/2) + (1 -(level1%2))*bonus
	valor2 = ((ataque2+defesa2)/2) + (1 -(level2%2))*bonus
	if valor1 > valor2 :
		print("Dabriel")
	elif valor2 > valor1 :
		print("Guarte")
	else :
		print("Empate")