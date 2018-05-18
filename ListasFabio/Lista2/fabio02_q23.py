"""
	Questão: Lista 2 23
	Descrição: receba duas datas e diga qual das duas é a mais recente
"""

def main():
	#entrada
	dia1 = int(input("digite o dia da primeira data: "))
	mes1 = int(input("digite o mes da primeira data: "))
	ano1 = int(input("digite o ano da primeira data: "))
	dia2 = int(input("digite o dia da segunda data: "))
	mes2 = int(input("digite o mes da segunda data: "))
	ano2 = int(input("digite o ano da segunda data: "))
	#processamento
	if ano1 > ano2 :
		data = 1
	elif ano2 > ano1 :
		data = 2
	else :
		if mes1 > mes2 :
			data = 1
		elif mes2 > mes1 :
			data = 2
		else:
			if dia1 > dia2 :
				data = 1
			elif dia2 > dia1 :
				data = 2
			else :
				data = 0
	#saida
	if data == 0 :
		print("as datas são iguais")
	else :
		print("a data %d é mais recente: " %data)

if __name__ == '__main__':
	main()
