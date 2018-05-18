"""
	Questão: Lista 1 16
	Descrição: lê valor do lado de um quadrado e devolve a area do quadrado
"""
def main():
	#entrada
	lado = float(input("digite o tamanho do lado do quadrado: "))
	#processamento
	area = lado**2
	#saida
	print("a area do quadrado é igual a %.2f" %area)

if __name__ == '__main__':
	main()