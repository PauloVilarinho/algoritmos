"""
	Questão: Lista 1 21
	Descrição: lê uma temperatura em graus fahrenheit e devolve em graus celcius
"""

def  main():
	#entrada
	graus_f = float(input("digite a temperatura em graus fahrenheit: "))
	#processamento
	graus_c = (5*graus_f-160)/9
	#saida
	print("a temperatura em graus celcius é %.1f°C" %graus_c)

if __name__ == '__main__':
	main()