"""
	Questão: Lista 2 26
	Descrição: le os 3 lados do triangulo e identifique quais são os catetos e qual é a hipotenusa
"""

def main():
	#entrada
	ladoa = float(input("digite o tamanho do lado A: "))
	ladob = float(input("digite o tamanho do lado B: "))
	ladoc = float(input("digite o tamanho do lado C: "))
	#processamento
	if ladoa > ladob:
		if ladoa>ladoc:
			hipotenusa = ladoa
		else:
			hipotenusa = ladoc
	else:
		if ladob>ladoc:
			hipotenusa = ladob
		else:
			hipotenusa = ladoc
	#saida
	print("a hipotenusa do quadrado é igual a %.2f" %hipotenusa)

	
if __name__ == '__main__':
	main()
