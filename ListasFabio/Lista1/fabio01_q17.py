"""
	Questão: Lista 1 17
	Descrição: lê valor da base a altura do retangulo e devolve area do retangulo
"""

def main():
	#entrada
	base = float(input("Digite o valor da base do retangulo: "))
	altura = float(input("Digite o valor da altura do retangulo:  "))
	#processamento
	area = base*altura
	#saida
	print("area do retangulo é igual a %.2f" %area)

if __name__ == '__main__':
	main()