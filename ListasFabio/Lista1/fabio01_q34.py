'''
	Questão Lista 1 32
	Descrição lê 3 numeros e devolve a media dos 3 numeros
'''
def main():
	#entrada
	numeros = [int(i) for i in input("digite 3 numeros: ").split()]
	#processamento
	total = 0
	for i in numeros:
		total += i
	media = total/len(numeros)
	#saida
	print("a media dos numeros inseridos é igual a %.2f" %media)
	

if __name__ == '__main__':
	main()