"""
	Questão: Lista 1 19
	Descrição: lê valor do raio de uma esfera e devolve o valor do volume da esfera
"""

def main():
	#entrada
	raio = float(input("digite o valor do raio da esfera: "))
	#processamento
	volume = (4*3.14*(raio**3))/3
	#saida
	print("o volume da esfera é igual a %.2f " %volume)

if __name__ == '__main__':
	main()