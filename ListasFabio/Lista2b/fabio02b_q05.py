"""
	Questão: Lista 2b 05
	Descrição: receba 3 preços retonar qual o mais barato
"""

def main():
    #entrada
    produto1 = float(input("digite o preço do produto 1: "))
    produto2 = float(input("digite o preço do produto 2: "))
    produto3 = float(input("digite o preço do produto 3: "))
    #processamento
    if produto1 <= produto2 :
        if produto1 < produto3 :
            maisbarato = 1
        elif produto3 < produto2 :
            maisbarato = 3
        else :
            maisbarato = 1
    elif produto2 < produto1 :
        if produto2 < produto3 :
            maisbarato = 2
        elif produto3 < produto1 :
            maisbarato = 3
        else :
            maisbarato = 2

    #saida
    print("o produto mais barato é o produto %d" %maisbarato)

if __name__ == '__main__':
    main()
