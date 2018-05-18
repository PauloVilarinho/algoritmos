"""
	Questão: Lista 1 04
	Descrição: converter um valor em dolar para reais
"""

def main():
	#entrada
	valor_dolar = float(input("Digite o valor da cotacao do dolar hoje: "))
	quantidade_dolar = float(input('Digite a o valor em dolar a ser convetido: '))
	#processamento
	quantidade_reais = quantidade_dolar*valor_dolar	
	#saida 
	print("valor convertido em reais = R$ %.2f" %quantidade_reais)

if __name__ == '__main__':
	main()
			