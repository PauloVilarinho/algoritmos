ruas,inteiros = [int(i) for i in input().split()]
case = 0
while ruas != 0 or inteiros!=0 :
	quantity = 0
	case += 1
	while ruas>inteiros :
		ruas -= inteiros
		quantity += 1
	if quantity >26 :
		print("Case %d: impossible" %case)
	else :
		print("Case %d: %d" %(case,quantity))
	ruas,inteiros = [int(i) for i in input().split()]