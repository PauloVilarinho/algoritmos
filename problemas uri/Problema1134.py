num = 0
alc = 0
gas = 0
die = 0

while num !=4 :
	num =  int(input())
	if num == 1:
		alc = alc + 1
	elif num == 2:
		gas = gas + 1
	elif num == 3:
		die = die + 1
print ("MUITO OBRIGADO")
print("Alcool: %d" %alc)
print("Gasolina: %d" %gas)
print("Diesel: %d" %die)