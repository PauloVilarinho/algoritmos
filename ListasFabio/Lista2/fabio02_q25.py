"""
	Questão: Lista 2 25
	Descrição: recebe uma senha e verifica se é a certa
"""

def main():
	#entrada
	senha = input("digite sua senha:")
	#processamento
	if senha == "1234" :
		acesso = True
	else :
		acesso = False

	#saida
	if acesso :
		print("acesso permitido")
	else :
		print("acesso engado")
if __name__ == '__main__':
	main()
