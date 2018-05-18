"""
	Questão: Lista 1 08
	Descrição: lê 2 numeros e calcula a divisão da soma pela subtraçao dos dois numeros 
"""

def main():
	#entrada
	numero1 = int(input("digite o nuemro 1:"))
	numero2 = int(input("digite o nuemro 2:"))
	#processamento
	soma =  numero2+numero1
	diferenca = numero1-numero2
	divisao = soma/diferenca
	#saida
	print("a divisão da soma pela subtração é: %.2f" %divisao)

if __name__ == '__main__':
	main()