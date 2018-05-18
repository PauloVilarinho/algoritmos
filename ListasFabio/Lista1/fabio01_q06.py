"""
	Questão: Lista 1 06
	Descrição: converte velocidade em kilometros por hora para metros por segundo
"""

def main():
	#entrada
	velocidade_kilometro = float(input("Digite a velocidade em kilometros por hora: "))
	#processamento
	velocidade_metros = velocidade_kilometro/3.6
	#saida
	print("A velocidade em metros por segundo é: %.2fm/s" %velocidade_metros)

if __name__ == '__main__':
	main()