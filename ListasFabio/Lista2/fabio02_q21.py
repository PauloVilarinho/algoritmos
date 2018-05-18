"""
	Questão: Lista 2 21
	Descrição: arredonda numeros decimais
"""

def main():
	#entrada
	numero = float(input("insira um numero: "))
	#processamento
	if numero%1 < 0.5 :
		arredondado = numero//1
	else :
		arredondado = (numero//1) + 1
	#saida
	print("o numero arredondado é  %d" %arredondado)

if __name__ == '__main__':
	main()
