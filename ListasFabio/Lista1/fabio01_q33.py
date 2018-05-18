'''
	Questão Lista 1 33
	Descrição lê um numero de 3 digitos e calcula a soma entre o numero e seu inverso
'''
def main():
	#entrada
	numero = input("insira um numero de 3 digitos: ")
	#processamento
	inverso = numero[::-1]
	soma = int(numero) + int(inverso)
	#saida
	print("a soma entre o numero e o seu inverso é de %d" %soma)

if __name__ == '__main__':
	main()