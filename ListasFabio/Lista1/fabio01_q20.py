"""
	Questão: Lista 1 20
	Descrição: lê uma temperatura em graus celcius e devolve em graus farenhit
"""

def main():
	#entrada
	graus_C = float(input("insira a temperatura em graus celcius: "))
	#processamento
	graus_F = (9*graus_C+160)/5
	#saida
	print("a temperatura em graus fahrenheit é: %.1f°F" %graus_F)

if __name__ == '__main__':
	main()