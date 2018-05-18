"""
	Questão: Lista 1 30
	Descrição: lê um valor de tempo em minutos e retorna o valor em dias horas e minutos
"""

def main():
	#entrada
	minutos = int(input("digite o valor de tempo em minutos: "))
	#processamento
	dias = minutos//1440
	minutos -= dias*1440
	horas = minutos//60
	minutos -= horas*60
	#saida
	print("o valor de tempo inserido é igual a %d dias, %d horas e %d minutos" %(dias,horas,minutos))

if __name__ == '__main__':
	main()