"""
	Questão: Lista 2 17
	Descrição: faça calculos difentes baseado no resto da divisão entre dois numeros
"""

def main():
	#entrada
	numero1 = int(input("digite o numero 1: "))
	numero2 = int(input("digite o numero 2: "))
	#processamento
	resto = numero1%numero2

	if resto == 1 :
		total = numero1 + numero2 + resto
		resposta = str(total)
	elif resto == 2 :
		if numero1%2 == 0 :
			resultado1 = "numero1 é par"
		else:
			resultado1 = "numero1 é impar"
		if numero2%2 == 0 :
			resultado2 = "numero2 é par"
		else:
			resultado2 = "numero2 é impar"
		resposta = resultado1 + " e " + resultado2
	elif resto == 3 :
		total = (numero1 + numero2)*numero1
		resposta = str(total)
	elif (resto == 4) and (numero2 != 0) :
		total = (numero1 + numero2)/numero2
		resposta = str(total)
	else :
		valor1 = numero1**2
		valor2 = numero2**2
		resposta = str(valor1) + " e " + str(valor2)

	#saida
	print("a resposta é %s" %resposta)

if __name__ == '__main__':
	main()