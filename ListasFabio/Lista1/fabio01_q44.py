'''
	Questão Lista 1 44
	Descrição retorna a quantidade de cobre e zinco em uma daa quantidade de latão
'''

def main():
	#entrada
	peso_latao = float(input("digite a quantidade de latão em kg: "))
	#processamento
	peso_cobre = peso_latao*0.7
	peso_zinco = peso_latao*0.3
	#saida
	print("nesse peso de latão tem %.2fKg de cobre e %.2fKg de zinco" %(peso_cobre,peso_zinco))

if __name__ == '__main__':
	main()