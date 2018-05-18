'''
	Questão Lista 1 42
	Descrição calcula a distancia entre dois pontos
'''

def main():
	#entrada
	x1,y1 = [float(i) for i in input("digite a cordenada x e y do ponto 1: ").split()]
	x2,y2 = [float(i) for i in input("digite a cordenada x e y do ponto 2: ").split()]
	#processamento
	distancia = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
	#saida
	print("distancia entre os dois pontos é %.2f" %distancia)

if __name__ == '__main__':
	main()