"""
	Questão: Lista 1 25
	Descrição: lê uma quantidade em metros e retorna essa quantidade em kilometros e metros
"""

def main():
	#entrada
	distancia_m = int(input("digite uma distancia em metros: "))
	#processamento
	valor_km = distancia_m//1000
	valor_m = distancia_m%1000
	#saida
	print("a distancia é igual a %dkm e %dm" %(valor_km,valor_m))

if __name__ == '__main__':
	main()