"""
	Questão: Lista 2b 15
	Descrição: retorna o preco a ser pago no mercado
"""

def main():
    #entrada
    macakilos = float(input("quantos kilos de maçã foram comprados?"))
    morangokilos = float(input("quantos kilos de morango foram comprados?"))
    #processamento
    total = morangokilos + macakilos

    if morangokilos > 5 :
        morangopreco = 2.2
    else :
        morangopreco = 2.5
    if macakilos > 5 :
        macapreco = 1.8
    else :
        macapreco = 1.5

    preco = morangokilos*morangopreco + macakilos*macapreco
    if total >=8 :
        preco = preco*0.9
    #saida
    print(preco)

if __name__ == '__main__':
    main()
