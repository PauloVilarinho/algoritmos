"""
	Questão: Lista 1 05
	Descrição: soma os algarismos de um numero de 3 digitos
"""
def main():
	#entrada
	centenas,dezenas,unidades = [int(i) for i in list(input("Digite um numero de 3 digitos: "))]
	#processamento
	total = centenas+dezenas+unidades
	#saida
	print("A soma dos digitos desse numero é: %d" %total)

if __name__ == '__main__':
	main()