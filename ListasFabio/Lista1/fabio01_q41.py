'''
	Questão Lista 1 41
	Descrição calcula o custo do carro para o cliente
'''

def main():
	#entrada
	preco_fabrica = float(input("digite o preço de fabrica de um carro: "))
	#processamento
	imposto = preco_fabrica*0.45
	lucro = preco_fabrica*0.28
	preco_consumidor = preco_fabrica + imposto + lucro
	#saida
	print("preço para o consumidor = %.2fR$" %preco_consumidor)

if __name__ == '__main__':
	main()