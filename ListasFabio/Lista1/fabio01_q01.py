"""
	Questão: Lista 1 01
	Descrição: converter velocidade em metros por segundo para kilometros por hora
"""

def main():
	#entrada
	velocidade_metros = float(input('Digite a velocidade em metros por segundo: '))
	#processamento
	velocidade_kilometros = velocidade_metros*3.6
	#saida
	print("velocidade em kilometros por hora: %.2f" %velocidade_kilometros)


if __name__ == '__main__':
	main()