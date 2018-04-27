quantity = int(input())
dentro = 0
fora = 0

for x in range(quantity):
	number = int(input())
	if 10<=number<=20 :
		dentro = dentro + 1
	else:
		fora = fora + 1

print (dentro, "in")
print (fora, "out")