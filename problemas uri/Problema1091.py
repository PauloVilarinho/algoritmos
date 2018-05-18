quantity = int(input())

while quantity != 0 :
	origemx,origemy = [int(i)  for i in input().split()]
	for i in range (quantity):
		pontox,pontoy = [int(i) for i in input().split()]
		if pontox == origemx or pontoy == origemy :
			print("divisa")
		elif pontox>origemx and pontoy>origemy:
			print("NE")
		elif pontox<origemx and pontoy>origemy:
			print("NO")
		elif pontox>origemx and pontoy<origemy:
			print("SE")
		elif pontox<origemx and pontoy<origemy:
			print("SO")
	quantity = int(input())	