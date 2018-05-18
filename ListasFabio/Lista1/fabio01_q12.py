"""
	Questão: Lista 1 12
	Descrição: lê o salario de um trabalhador e devolve o salario com um aumento de 25% 
"""

def main():
	#entrada
	salario = float(input("Insira o seu salario: "))
	#processamento
	novo_salario = salario*(1.25)
	#saida
	print("O seu novo salario é igual a %.2f" %(novo_salario))

if __name__ == '__main__':
	main()