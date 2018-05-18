"""
	Questão: Lista 1 23
	Descrição: lê um valor em kilogramas e devolve o valor em gramas
"""

def main():
	#entrada
	peso_kg = float(input("digite o valor em kilogramas: ").strip("Kg"))
	#processamento
	peso_g = peso_kg*1000
	#saida
	print("o peso em kilogramas é igual a %.2fg" %peso_g)

if __name__ == '__main__':
	main()