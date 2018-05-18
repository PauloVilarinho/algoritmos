'''
	Questão Lista 1 45
	Descrição calcula a melhor forma de entregar o dinheiro de um caixa eletronico
'''

def main():
	#entrada
	valor_solicitado = int(input("digite quanto o valor a ser retirado do caixa(notas disponiveis: 50, 10, 5, 1):"))
	#processamento
	notas50 = valor_solicitado//50
	valor_solicitado -= notas50*50
	notas10 = valor_solicitado//10
	valor_solicitado -= notas10*10
	notas5 = valor_solicitado//5
	valor_solicitado -= notas5*5
	notas1 = valor_solicitado
	
	#saida
	print("%d notas de 50, %d notas de 10, %d notas de 5, %d notas de 1" %(notas50,notas10,notas5,notas1))

if __name__ == '__main__':
	main()