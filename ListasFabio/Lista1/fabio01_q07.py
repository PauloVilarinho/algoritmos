"""
	Questão: Lista 1 07
	Descrição: lê 3 numeros e calcula a soma dos dois primeiros e a diferenca dos dois ultimos
"""

def main():
	#entrada
	numeroa = int(input("digite numero 1: "))
	numerob = int(input("digite numero 2: "))
	numeroc = int(input("digite numero 3: "))
	#processamento
	soma = numeroa + numerob
	diferenca = numerob - numeroc
	#saida 
	print("a soma dos dois primeiros é: %d" %soma)
	print("a diferença entre os dois ultimos é: %d " %diferenca)

if __name__ == '__main__':
	main()