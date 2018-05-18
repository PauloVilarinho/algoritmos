"""
	Questão: Lista 2 16
	Descrição: calcula aprovação de um aluno
"""

def main():
	#entrada
	nota1 = float(input("digite sua primeira nota: "))
	nota2 = float(input("digite sua segunda nota: "))
	#processamento
	media = (nota1+nota2)/2
	if media >= 7 :
		resultado = "Aprovado"
	else :
		exame_final = float(input("digite a nota do seu exame final: "))
		media = (media+exame_final)/2
		if media >= 5 :
			resultado = "Aprovado"
		else :
			resultado = "Reprovado"
	#saida
	print("O aluno está %s" %resultado)

if __name__ == '__main__':
	main()