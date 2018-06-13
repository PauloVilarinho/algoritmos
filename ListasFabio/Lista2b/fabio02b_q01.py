"""
	Questão: Lista 2b 01
	Descrição: receba 1 numero e retorne se ele é positivo ou não
"""

def main():
    #entrada
    numero = float(input("digite um numero: "))
    #processamento
    if numero > 0 :
        positivo = True
    else :
        positivo = False
    #saida

    if positivo:
        print("numero é positivo")
    else :
        print("numero é negativo")

if __name__ == '__main__':
    main()
