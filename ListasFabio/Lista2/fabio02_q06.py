"""
	Questão: Lista 2 06
	Descrição: le 3 angulos e retorna se formam um triangulo e o tipo de triangulo formado
"""

def main():
	#entrada
	angulo1 = int(input("digite o primeiro angulo: "))
	angulo2 = int(input("digite o segundo angulo: "))
	angulo3 = int(input("digite o terceiro angulo: "))
	#processamento
	somatorio = angulo1 + angulo2 + angulo3
	if somatorio != 180 :
		triangulo = False
	else :
		triangulo = True
		if angulo1 > 90 or angulo2> 90 or angulo3 > 90 :
			tipo = "obtusangulo"
		elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90 :
			tipo = "retangulo"
		else :
			tipo = "acutangulo"	
	#saida
	if triangulo :
		print("é possivel formar triangulo e forma um triangulo %s" %tipo)
	else :
		print("não forma triangulo")

if __name__ == '__main__':
	main()