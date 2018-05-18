'''
	Questão Lista 1 46
	Descrição calcula o valor da entrada e das parcelas
'''

def main () :
	#entrada
	valor_mercadoria = int(input("digite o valor da mercadoria: "))
	#processamento
	parcela = valor_mercadoria//3
	entrada = parcela + valor_mercadoria%3
	#saida
	print("o produto sera vendido a R$ %.2f na entrada e R$ %.2f nas parcelas" %(entrada,parcela))

if __name__ == '__main__':
	main()
