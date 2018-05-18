quantity = int(input())
case = 0
for i in range(quantity):
	case += 1
	lista = input().split()
	jogadores = int(lista[0])
	lider = (jogadores//2)+1
	print("Case %d: %i" %(case,int(lista[lider])))