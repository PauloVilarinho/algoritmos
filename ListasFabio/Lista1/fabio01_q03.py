"""
	Questão: Lista 1 03
	Descrição: converter horario em minutos para horario em horas e minutos
"""

def main() :
	#entrada
	horario = int(input('digite um horario em minutos: '))
	#processamento
	horas = horario//60
	minutos	= horario%60
	#saida
	print("horario em horas e minutos: %02d:%02d" %(horas,minutos))

if __name__ == '__main__':
	main()