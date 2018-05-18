"""
	Questão: Lista 1 22
	Descrição: lê um valor em kilometros e devolve o valor em metros
"""

def main():
	#entrada
	distancia_km = float(input("digite o valor da distancia em km: "))
	#processamento
	distacia_m = distancia_km*1000
	#saida
	print("a distancia em metros é igual a %.2f" %distacia_m)

if __name__ == '__main__':
	main()