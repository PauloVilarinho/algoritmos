"""
	Questão: Lista 2 01
	Descrição: recebe 3 numeros e devolve quantos deles são iguais
"""

def main():
	#entrada
	numero1 = int(input("Digite o primeiro numero: "))
	numero2 = int(input("Digite o segundo numero: "))
	numero3 = int(input("Digite o terceiro numero: "))
	#processamento
	if numero1 == numero2 :
		if numero2 == numero3 :
			total = 3
		else :
			total = 2
	elif numero2 == numero3 :
		total = 2
	elif numero1 == numero3 :
		total = 2
	else :
		total = 0
	#saida
	print("a quantidade de numeros iguais é %d" %total)

if __name__ == '__main__':
	main()