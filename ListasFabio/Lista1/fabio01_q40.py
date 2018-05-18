'''
	Questão Lista 1 40
	Descrição : calcula o dinheiro gasto em cigarros
'''

def main():
	#entrada
	anos_fumando = int(input("digite a quantos anos voce fuma: "))
	cigarros_dia = int(input("quantos cigarros voce fuma por dia: "))
	preco_carteira = float(input("qual o preço da carteira de cigarro?"))
	#processamento
	tempo = anos_fumando*360
	cigarros = cigarros_dia*tempo
	carteiras = cigarros/20
	if carteiras> int(carteiras) :
		carteiras = int(carteiras) + 1
	dinheiro = carteiras*preco_carteira
	#saida
	print("o dinheiro gasto com cigarros foi %.2fR$" %dinheiro)

if __name__ == '__main__':
	main()