while True:		
	try:
		palavra = list(input())
		d = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
		total = 0
		for i in palavra :
			d[i] = d[i] + 1
			total += 1

		def fac(x):
			if x == 0 :
				return 1
			valor = 1
			for i in range (x):
				valor = valor*(i+1)
			return valor

		denominador = fac(d["A"])*fac(d["B"])*fac(d["C"])*fac(d["D"])*fac(d["E"])*fac(d["F"])*fac(d["G"])*fac(d["H"])*fac(d["I"])*fac(d["J"])*fac(d["K"])*fac(d["L"])*fac(d["M"])*fac(d["N"])*fac(d["O"])*fac(d["P"])*fac(d["Q"])*fac(d["R"])*fac(d["S"])*fac(d["T"])*fac(d["U"])*fac(d["V"])*fac(d["W"])*fac(d["X"])*fac(d["Y"])*fac(d["Z"])
		numerador = fac(total)
		resultado = (numerador//denominador)
		print(resultado%1000000007)
	except EOFError :
		break