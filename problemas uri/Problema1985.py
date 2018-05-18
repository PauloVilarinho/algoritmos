quantity = int(input())
total = 0

cardapio = {1001 : 1.50 , 1002 : 2.50 , 1003: 3.50, 1004: 4.50 , 1005: 5.50}

for i in range(quantity):
	produto,unidades = [int(i) for i in input().split()]
	total = total + cardapio[produto]*unidades

print("%.2f" %total)