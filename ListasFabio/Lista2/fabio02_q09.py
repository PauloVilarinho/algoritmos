"""
	Questão: Lista 2 09
	Descrição: le 1 numero de 0 a 100 e retorna se é primo ou não
"""

def main() :
	#entrada
	numero = int(input("digite um numero de 0 a 100: "))
	#processamento
	
	if numero == 2 or numero == 3 or numero == 5 or numero == 7 :
		primo = True
	elif numero%2 == 0 :
		primo = False
	elif numero%3 == 0 :
		primo = False
	elif numero%5 == 0 :
		primo = False
	elif numero%7 == 0 :
		primo = False
	else :
		primo = True
	#saida
	if primo :
		print("o numero inserido é primo")
	else :
		print("o numero inserido não é primo")

if __name__ == '__main__':
	main()