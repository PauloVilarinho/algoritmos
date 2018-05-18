'''
	Questão Lista 1 36
	Descrição lê a idade de uma pessoa expressa em anos meses e dias e devolve expressa somente em dias
'''
def main():
	#entrada
	anos,meses,dias = [int(i) for i in input("digite sua idade no seguinte formato(anos meses dias): ").split()]
	#processamento
	idade_dias = anos*360 + meses*30 +dias
	#saida
	print("a sua idade em dias é %d" %idade_dias)
	

if __name__ == '__main__':
	main()