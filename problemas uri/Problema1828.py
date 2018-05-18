quantity = int(input())
case = 0
for i in range (quantity):
	sheldon,raj = [i for i in input().split()]
	rajwins = False
	sheldonwins = False
	case += 1
	if sheldon == "papel" :
		if raj == "tesoura" or raj == "lagarto" :
			rajwins = True
		elif raj == "Spock" or raj == "pedra" :
			sheldonwins = True
	elif sheldon == "tesoura" :
		if raj == "pedra" or raj == "Spock" :
			rajwins = True
		elif raj == "lagarto" or raj == "papel" :
			sheldonwins = True
	elif sheldon == "pedra" :
		if raj == "papel" or raj == "Spock" :
			rajwins = True
		elif raj == "lagarto" or raj == "tesoura" :
			sheldonwins = True
	elif sheldon == "Spock" :
		if raj == "papel" or raj == "lagarto" :
			rajwins = True
		elif raj == "pedra" or raj == "tesoura" :
			sheldonwins = True
	elif sheldon == "lagarto" :
		if raj == "pedra" or raj == "tesoura" :
			rajwins = True
		elif raj == "Spock" or raj == "papel" :
			sheldonwins = True

	if sheldonwins :
		print("Caso #%d: Bazinga!" %case)
	elif rajwins :
		print("Caso #%d: Raj trapaceou!" %case)
	else :
		print("Caso #%d: De novo!" %case)