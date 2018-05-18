"""
	Questão: Lista 2 29
	Descrição: retorna se um numero é um quadrado perfeito ou não
"""

def main():
	#entrada
	numero = int(input("digite um numero de quatro digitos: "))
	#processamento
	grupo1 = numero//100
	grupo2 = numero%100
	raiz = numero**(1/2)
	if (raiz == grupo2+grupo1) :
		quadrado = True
	else :
		quadrado = False

	#saida
	if quadrado :
		print("O numero é um quadrado perfeito.")
	else :
		print("O numero não é um quadrado perfeito.")

if __name__ == '__main__':
	main()