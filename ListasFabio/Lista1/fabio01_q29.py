"""
	Questão: Lista 1 29
	Descrição: lê um valor de tempo em meses e retorna esse valor de tempo em anos e meses
"""

def main():
	#entrada
	tempo_meses = int(input("digite o valor de tempo em meses: "))
	#processamento
	valor_anos = tempo_meses//12
	valor_meses = tempo_meses%12
	#saida
	print("o valor inserido é igual a %d anos e %d meses" %(valor_anos,valor_meses))

if __name__ == '__main__':
	main()