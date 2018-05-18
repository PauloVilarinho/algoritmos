'''
	Questão Lista 1 31
	Descrição lê um numero binario de 4 digitos e retorna o valor em decimal
'''

def main():
	#entrada
	numero_bin = [int(i) for i in list(input("digite um numero em binario:"))]
	#processamento
	numero_bin.reverse()
	total = 0
	for i in range(len(numero_bin)):
		total += numero_bin[i]*(2**i)
	#saida
	print("o numero binario inserido em decimal e igual a %d" %total)

if __name__ == '__main__' :
	main()