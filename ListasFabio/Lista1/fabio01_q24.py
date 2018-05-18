"""
	Questão: Lista 1 24
	Descrição: lê um valor em metro e devolve o valor em centimetros
"""

def main():
	#entrada
	distancia_m = float(input("digite a distancia em metros:"))
	#processamento
	distancia_cm = distancia_m*100
	#saida
	print("a distancia em centimetros é igual a %.2fcm" %distancia_cm)

if __name__ == '__main__':
	main()