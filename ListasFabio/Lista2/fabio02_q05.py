"""
	Questão: Lista 2 05
	Descrição: le 3 numeros e os escreve em ordem decrescente
"""

def main():
	#entrada
	numero1 = int(input("digite o numero 1: "))
	numero2 = int(input("digite o numero 2: "))
	numero3 = int(input("digite o numero 3: "))
	#processamento
	maior,meio,menor = sort3num(numero1,numero2,numero3)
	#saida
	print("%d %d %d" %(maior,meio,menor))

# *** funçõesauxiliares **
def sort3num(a,b,c):
	if a>b :
		if a>c :
			maior = a
			if c>b :
				menor = b
				meio = c
			else :
				menor = c
				meio = b
		else :
			maior = c
			meio = a
			menor = b
	else :
		if b>c :
			maior = b
			if c>b :
				menor = a
				meio = c
			else :
				menor = c
				meio = a
		else :
			maior = c
			meio = b
			menor = a

	return maior,meio,menor


if __name__ == '__main__':
	main()