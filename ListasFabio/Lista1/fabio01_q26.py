"""
	Questão: Lista 1 26
	Descrição: lê um numero inteiro de dias e devolve o valor em numero de semanas e dias
"""

def main():
	#entrada
	quantidade_dias = int(input("digite a quantidade de dias: "))
	#processamento
	valor_dias = quantidade_dias%7
	valor_semanas = quantidade_dias//7
	#saida
	print("o tempo digitado é igual a %d semanas e %d dias" %(valor_semanas,valor_dias))

if __name__ == '__main__':
	main()