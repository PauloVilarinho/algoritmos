"""
	Questão: Lista 1 15
	Descrição: lê valor de base e altura de um triangulo e devolve a area do triangulo
"""

def main():
	#entrada
	base = float(input("digite o valor da base do triangulo: "))
	altura = float(input("digite a altura do traingulo relativa a base inserida: "))
	#processamento
	area = (base*altura)/2
	#saida
	print("A area do triangulo é: %.2f" %area)

if __name__ == '__main__':
	main()