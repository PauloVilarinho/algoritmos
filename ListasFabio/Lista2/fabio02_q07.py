"""
	Questão: Lista 2 07
	Descrição: le 3 lados de um triangulo se formam um triangulo e o tipo de triangulo formado
"""

def main():
	#entrada
	ladoa = float(input("coloque o valor do lado a: "))
	ladob = float(input("coloque o valor do lado b: "))
	ladoc = float(input("coloque o valor do lado c: "))
	#processamento
	if (abs(ladob - ladoc) < ladoa < ladob + ladoc) and (abs(ladoa - ladoc) < ladob < ladoa + ladoc) and (abs(ladoa - ladob) < ladoc < ladoa + ladob) :
		triangulo = True
		if ladoa == ladob :
			if ladob == ladoc :
				tipo = "equilatero"
			else :
				tipo = "isoceles"
		elif ladob == ladoc :
			tipo = "isoceles"
		elif ladoa == ladoc :
			tipo = "isoceles"
		else :
			tipo = "escaleno"
	else :
		triangulo = False

	#saida

	if triangulo :
		print("o triangulo é possivel de ser formado e é do tipo %s" %tipo)
	else :
		print("não é possivel formar um triangulo com esses lados")

if __name__ == '__main__':
	main()