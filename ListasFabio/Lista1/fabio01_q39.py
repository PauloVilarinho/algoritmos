'''
	Questão Lista 1 39
	Descrição lê tres numero inteiros e calcula  aexpressão
'''

def main():
	#entrada
	numeroa,numerob,numeroc = [int(i) for i in input("digite tres numeros inteiros: ").split()] 
	#processamento
	valor = ((numeroa+numerob)**2 +  (numerob+numeroc)**2)/2
	#saida
	print("resultado = %.2f " %valor)

if __name__ == '__main__':
	main()