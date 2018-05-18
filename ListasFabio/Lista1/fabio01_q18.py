"""
	Questão: Lista 1 18
	Descrição: lê valor do raio da circunferencia e devolve o comprimento da circunferencia
"""

def main():
	#entrada
	raio = float(input("digite o valor do raio da circunferencia: "))
	#processamento
	comprimento = 2*raio*3.1415
	#saida
	print("o comprimento da circunferencia é igual a %.2f" %comprimento)

if __name__ == '__main__':
	main()