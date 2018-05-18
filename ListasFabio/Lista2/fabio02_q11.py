"""
	Questão: Lista 2 11
	Descrição: recebe 4 numeros e printa o numero da opção escolhina no primeiro numero
"""

def main():
	#entrada
	option = int(input("escreva a opção a ser executada: "))
	num1 = int(input("digite o numero 1: "))
	num2 = int(input("digite o numero 2: "))
	num3 = int(input("digite o numero 3: "))
	#processamento
	if option == 1 :
		numero_mostrado = num1
	elif option == 2 :
		numero_mostrado = num2
	elif option == 3 :
		numero_mostrado = num3
	#saida
	print("numero =  %d " %numero_mostrado)

if __name__ == '__main__':
	main()