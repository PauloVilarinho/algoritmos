"""
	Questão: Lista 2 10
	Descrição: recebe uma data e retorna ela se ela for valida
"""

def main():
	#entrada
	dia = int(input("digite o dia da data: "))
	mes = int(input("digite o mes da data: "))
	ano = int(input("digite o ano da data: "))
	#processamento
	validade = datavalida(dia,mes,ano)
	#sadia
	if validade :
		print("%d/%d/%d" %(dia,mes,ano))
	else :
		print("data invalida")


def datavalida(d,m,a) :
	if d <= 0 or m <= 0 or a <= 0 :
		return False
	elif d>30 or m >12 :
		return False
	else :
		return True


if __name__ == '__main__':
	main()