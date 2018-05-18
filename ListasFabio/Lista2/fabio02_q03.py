"""
	Questão: Lista 2 03
	Descrição: le 3 numeros e retorna o maior entre eles
"""

def main():
	#entrada
	numero1 = float(input("digite o numero 1: "))
	numero2 = float(input("digite o numero 2: "))
	numero3 = float(input("digite o numero 3: "))
	#processamento
	if numero1 > numero2 :
		if numero1 > numero3 :
			maior = numero1
		else :
			maior = numero3
	else :
		if numero2 > numero3 :
			maior = numero2
		else :
			maior = numero3

	#saida
	print("o maior nummero é %.2f" %maior)

if __name__ == '__main__':
	main()