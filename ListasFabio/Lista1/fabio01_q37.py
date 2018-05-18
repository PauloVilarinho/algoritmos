'''
	Questão Lista 1 37
	Descrição lê a idade de uma pessoa expressa em dias e retorna a idade em dias meses e anos
'''
def main():
	#entrada
	dias = int(input("digite a sua idade em dias: "))
	#processamento
	anos = dias//360
	dias -= anos*360
	meses = dias//30
	dias -= meses*30
	#saida
	print("sua idade é de %d anos, %d meses e %d dias" %(anos,meses,dias))
	

if __name__ == '__main__':
	main()