while True :


	try:
		numero = list(input())
		while numero[len(numero) - 1] != "#" :
			numero += list(input())
		numero.pop()
		numero.reverse()
		while numero[len(numero) - 1] == 0:
			numero.pop() 
		lenth = len(numero)
		total = 0
		for i in range(lenth):
				total += int(numero[i])*(2**i)
			
		if total%131071 == 0  :
			print("YES")
		else :
			print("NO")

	except EOFError:
		break