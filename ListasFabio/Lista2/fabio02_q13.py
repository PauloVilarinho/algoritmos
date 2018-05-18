"""
	Questão: Lista 2 13
	Descrição: recebe 5 numeros e retorna o maior e o menor
"""

def main():
	#entrada
	num1 = int(input("digite numero 1: "))
	num2 = int(input("digite numero 2: "))
	num3 = int(input("digite numero 3: "))
	num4 = int(input("digite numero 4: "))
	num5 = int(input("digite numero 5: "))
	#processamento
	maior,menor = maiormenor(num1,num2,num3,num4,num5)
	#saida
	print("maior numero : %d menor numero : %d " %(maior,menor))

def maiormenor(a,b,c,d,e):
	maior = a
	menor = a
	if b > maior :
		maior = b
	if b < menor :
		menor = b
	if c > maior :
		maior = c
	if c < menor :
		menor = c
	if d > maior :
		maior = d
	if d < menor :
		menor = d
	if e > maior :
		maior = e
	if e < menor :
		menor = e

	return maior,menor 
	
if __name__ == '__main__':
	main()