"""
	Questão: Lista 2 04
	Descrição: le 1 numero de 2 digitos e retornar se as dezenas são iguais as unidades ou n
"""

def main():
	#entrada
	numero = int(input("digite um numero de 2 algarismos: "))
	#processamento
	dezenas = numero//10
	numero -= dezenas*10
	unidade = numero
	if unidade == dezenas :
		igual = True
	else:
		igual = False
	#saida

	if igual:
		print("o algarismo das dezenas é igual ao das unidades")
	else:
		print("o algarismo das dezenas é diferente do das unidades")

if __name__ == '__main__':
	main()