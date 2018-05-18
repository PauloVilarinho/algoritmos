"""
	Questão: Lista 1 14
	Descrição: lê 3 notas e seus 3 pesos e devolve a media ponderada
"""

def main():
	#entrada
	nota1,nota2,nota3 = [float(i) for i in input("Ensira suas 3 notas: ").split()]
	peso1,peso2,peso3 = [int(i) for i in input("Ensira os 3 pesos respectivos as notas inseridas anteriormente: ").split()]
	#processamento
	media = ((nota1*peso1)+(nota2*peso2)+(nota3*peso3))/(peso1+peso2+peso3)
	#saida
	print("sua media final é igual a %.2f" %media)

if __name__ == '__main__':
	main()