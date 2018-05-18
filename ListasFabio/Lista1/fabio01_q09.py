"""
	Questão: Lista 1 09
	Descrição: lê 2 numeros e os coloca em ordem contraria 
"""

def main():
	#entrada
	numeros = input("Insira 2 numeros: ")
	#processamento
	numero1,numero2 = [int(i) for i in numeros.split()]
	#saida
	print(numero2,numero1)

if __name__ == '__main__':
	main()