'''
	Questão Lista 1 32
	Descrição lê um numero de 3 digitos e calcula a diferença entre o numero e seu inverso
'''
def main():
	#entrada
	numero = input("insira um numero de 3 digitos: ")
	#processamento
	inverso = numero[::-1]
	diferenca = int(numero) - int(inverso)
	#saida
	print("a diferença entre o numero e o seu inverso é de %d" %diferenca)

if __name__ == '__main__':
	main()