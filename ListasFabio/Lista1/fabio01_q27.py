"""
	Questão: Lista 1 27
	Descrição: lê um valor de tempo em segundos e retorna o valor em horas minutos e segundo
"""

def main():
	#entrada
	segundos = int(input("digite o valor de tempo em segundos: "))
	#processamento
	horas = segundos//3600
	segundos -= horas*3600
	minutos = segundos//60
	segundos -= minutos*60
	#saida
	print("o tempo inserido é igual a %d horas %d minutos %d segundos" %(horas,minutos,segundos))

if __name__ == '__main__':
	main()