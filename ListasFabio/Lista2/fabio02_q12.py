"""
	Questão: Lista 2 12
	Descrição: recebe um numero e retorna se ele é par ou não
"""

def main():
	#entrada
	numero = int(input("digite um numero: "))
	#processamento
	if numero%2 == 0 :
		tipo = "par"
	else :
		tipo = "impar"
	#saida
	print("o %d é %s" %(numero,tipo))

if __name__ == '__main__':
	main()