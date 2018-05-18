"""
	Questão: Lista 2 18
	Descrição: recebe 3 numeros e uma operação a ser realizada
"""

def main():
	#entrada
	numero1 = int(input("digite o numero 1: "))
	numero2 = int(input("digite o numero 2: "))
	operation = int(input("digite a operação a ser realizada: "))
	#processamento
	if operation == 1 :
		total = numero1 + numero2
	elif operation == 2 :
		total = numero1 - numero2
	elif operation == 3 :
		total = numero1 * numero2
	elif operation == 4 :
		total = numero1 / numero2
	#saida
	print("o resultado é %.2f" %total )

if __name__ == '__main__':
	main()