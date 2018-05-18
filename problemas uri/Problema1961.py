pulo,quantity = [int(i) for i in input().split()]

lista = input().split()

morreu = False

for i in range (quantity -1):
	if abs(int(lista[i])-int(lista[i+1])) > pulo :
		morreu = True

if morreu :
	print("GAME OVER")
else:
	print("YOU WIN")