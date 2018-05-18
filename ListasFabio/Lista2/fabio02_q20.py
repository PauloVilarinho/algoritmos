"""
	Questão: Lista 2 20
	Descrição: retorna quadrante do angulo inserido
"""

def main ():
	#entrada
	angulo = float(input("digite um angulo: "))
	#processamento
	if (0 <= angulo%360 < 90) :
		quadrante = 1
	elif (90 <= angulo%360 < 180) :
		quadrante = 2
	elif (180 <= angulo%360 < 270) :
		quadrante = 3
	else :
		quadrante = 4
	#saida
	print("o angulo se encontra no quadrante %d." %(quadrante	))

if __name__ == '__main__':
	main()