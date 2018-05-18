"""
	Questão: Lista 2 27
	Descrição: leia data atual e  data de nasciemtno do usuario e retorne idade em anos
"""

def main():
	#entrada
	dia_atual = int(input("digite o dia de hoje: "))
	mes_atual = int(input("digite o mes de hoje: "))
	ano_atual = int(input("digite o ano de hoje: "))
	dia_nascimento = int(input("digite o dia de seu nascimento: "))
	mes_nascimento = int(input("digite o mes de seu nascimento: "))
	ano_nascimento = int(input("digite o ano de seu nascimento: "))
	#processamento
	idade = ano_atual - ano_nascimento
	if mes_atual < mes_nascimento :
		idade -= 1
	elif mes_atual == mes_nascimento :
		if dia_atual < dia_nascimento :
			idade -= 1

	#saida
	print("a sua idade é de %d" %idade)

if __name__ == '__main__':
	main()