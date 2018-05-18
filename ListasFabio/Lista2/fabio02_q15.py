"""
	Questão: Lista 2 15
	Descrição: receba as horas aulas e o valor da hora aul de 2 professores e retorne qual ganha mais
"""


def main():
	#entrada
	horas_prof1 = int(input("digite a quantidade de horas aulas do professor 1: "))
	valor_hora_prof1 = float(input("digite o valor da hora aula do professor 1: "))
	horas_prof2 = int(input("digite a quantidade de horas aulas do professor 2: "))
	valor_hora_prof2 = float(input("digite o valor da hora aula do professor 2: ")) 
	#processamento
	salario1 = horas_prof1*valor_hora_prof1
	salario2 = horas_prof2*valor_hora_prof2
	if salario1>salario2 :
		professor = "professor 1"
	elif salario2>salario1 :
		professor = "professor 2"
	else :
		professor = "nenhum professor"
	#saida
	print("%s ganha mais " %professor)

	
if __name__ == '__main__':
	main()