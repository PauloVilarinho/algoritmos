
x = 1
y = 1
while (x != 0) and (y != 0):
	x,y = [int(i) for i in input().split()]
	if x>0 and y>0:
		print("primeiro")
	elif x<0 and y>0:
		print("segundo")
	elif x<0 and y<0:
		print("terceiro")
	elif x>0 and y<0:
		print("quarto")

