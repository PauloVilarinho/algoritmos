"""
	Questão: Lista 1 28
	Descrição: lê um valor de tempo em horas e retorna o valor em semanas dias e horas
"""

def main():
	#entrada
	horas = int(input("digite o valor de tempo em horas: "))
	#processamento
	semanas = horas//168
	horas -= semanas*168
	dias = horas//24
	horas -= dias*24
	#saida
	print("o tempo inserido é igual a %d semanas, %d dias e %d horas" %(semanas,dias,horas))

if __name__ == '__main__':
	main()