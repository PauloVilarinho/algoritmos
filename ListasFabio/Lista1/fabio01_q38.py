'''
	Questão Lista 1 38
	Descrição lê duas frações e retorna a soma
'''
def main():
	#entrada
	fração1 = input("digite a primeira fração (N/D): ").split("/")
	fração2 = input("digite a segunda fração (N/D): ").split("/")
	#processamento
	numerador = int(fração1[0])*int(fração2[1]) + int(fração2[0])*int(fração1[1])
	denominador = int(fração1[1])*int(fração2[1])
	#saida
	print("a soma é igual a %d/%d" %(numerador,denominador))
	

if __name__ == '__main__':
	main()