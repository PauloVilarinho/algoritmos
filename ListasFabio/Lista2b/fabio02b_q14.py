"""
	Questão: Lista 2b 14
	Descrição: retorna se o numero é decimal ou inteiro
"""

def main():
    #entrada
    tipo = input("qual o tipo de combustivel?")
    litros = float(input("quantos litros vão ser abastecidos?"))
    #processamento
    if litros >= 20 :
        if tipo == "G" :
            desconto = 6
            preco = 2.50
        elif tipo == "A" :
            desconto = 5
            preco = 1.90
    if litros < 20 :
        if tipo == "G" :
            desconto = 4
            preco = 2.50
        elif tipo == "A" :
            desconto = 3
            preco = 1.90

    total = preco*litros*((100-desconto)/100)
    #saida
    print("total de litros = %.2f" %total)

if __name__ == '__main__':
    main()
