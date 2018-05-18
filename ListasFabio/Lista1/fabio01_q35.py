'''
	Questão Lista 1 35
	Descrição lê um numero de 4 digitos e calcula a soma dos seus digitos
'''
def main():
	#entrada
	numero = [int(i) for i in list(input("digite um numero de 4 digitos: "))]
	#processamento
	total = 0
	for i in numero:
		total += i
	#saida
	print("o somatorio dos digitos do numeor é igual a %d" %total)
	

if __name__ == '__main__':
	main()