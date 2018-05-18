"""
	Questão: Lista 2 14
	Descrição: recebe 5 numeros e retorna os que estão acima da media
"""


def main():
	#entrada
	num1 = int(input("digite numero 1: "))
	num2 = int(input("digite numero 2: "))
	num3 = int(input("digite numero 3: "))
	num4 = int(input("digite numero 4: "))
	num5 = int(input("digite numero 5: "))
	#processamento
	media = (num1 + num2 + num3 + num4 + num5)/5
	texto = ""
	if media< num1 :
		texto = texto + " " + str(num1)
	if media< num2 :
		texto = texto + " " + str(num2)
	if media< num3 :
		texto = texto + " " + str(num3)
	if media< num4 :
		texto = texto + " " + str(num4)
	if media< num5 :
		texto = texto + " " + str(num5)
	#saida
	print("os numeros acima da media são(%s)" %texto)

if __name__ == '__main__':
	main()