"""
	Questão: Lista 2 28
	Descrição: le as cordenadas e calcula a area do triangulo
"""

def main():
	#entrada
	x = abs(int(input("digite a coordenada x: ")))
	y = abs(int(input("digite a coordenada y: ")))
	#processamento
	area = x*y

	#saida
	print("a area do retangulo é de %.2f" %area)

if __name__ == '__main__':
	main()