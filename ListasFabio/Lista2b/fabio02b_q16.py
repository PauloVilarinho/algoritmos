"""
	Questão: Lista 2b 16
	Descrição: retorna o preco a ser pago no mercado
"""

def main():
    #entrada
    tipo = input("qual o tipo de carne?")
    kilos = float(input("quanto kilos de carne?"))
    cartão = input("usa cartão tabajara?")
    #processamento
    if tipo == "file" :
        preco = 4.9
    elif tipo == "alcatra" :
        preco = 5.9
    elif tipo == "picanha" :
        preco = 6.9

    if kilos >=5 :
        preco += 0.9

    total = kilos*preco

    #saida
    print(total)
if __name__ == '__main__':
    main()
