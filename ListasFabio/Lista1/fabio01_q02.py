"""
	Questão: Lista 1 02
	Descrição: converter valor de tem em horas e minutos  para minutos
"""

def main():
	#entrada
	horario = input('digite um horario(HH:MM):')
	#processamento
	horas,minutos = [int(i) for i in horario.split(":")]
	horario_novo = horas*60 + minutos
	#saida
	print("horario em minutos: %d" %horario_novo)

if __name__ == '__main__':
	main()