"""
	Questão: Lista 1 13
	Descrição: lê um valor em real e devolve 70% desse valor 
"""

def main():
	#entrada
	valor = input("Insira o valor em R$: ")
	#processamento
	
	quantidade = float(valor.strip("R$"))
	resultado = quantidade*0.7
	#saida
	print("valor reduzido em 70%%: R$ %.2f " %resultado)

if __name__ == '__main__':
	main()