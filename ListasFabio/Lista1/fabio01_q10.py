"""
	Questão: Lista 1 10
	Descrição: lê 2 numeros e calcula o quociente e o resto da divisão 
"""

def main():
	#entrada
	numero1 = int(input("digite o primeiro numero: "))
	numero2 = int(input("digite o segundo numero: "))
	#processamento
	quociente = numero1//numero2
	resto = numero1%numero2
	#saida
	print("O quociente da divisão é %d e o resto da divisão é %d" %(quociente,resto))

if __name__ == '__main__':
	main()
