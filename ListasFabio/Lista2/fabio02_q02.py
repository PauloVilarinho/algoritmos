"""
	Questão: Lista 2 02
	Descrição: recebe 2 numeros e retorna qual é o maior e qual é o menor
"""

def main():
	#entrada
	numero1 = float(input("digite o numero 1: "))
	numero2 = float(input("digite o numero 2: "))
	#processamento
	maior = (numero1 + numero2 + abs(numero1 - numero2))/2
	menor = (numero1 + numero2 - abs(numero1 - numero2))/2
	#saida
	print("o maior numero é %.2f e o menor numero é %.2f" %(maior,menor))

if __name__ == '__main__':
	main()