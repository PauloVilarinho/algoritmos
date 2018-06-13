"""
	Questão: Lista 2b 12
	Descrição: retorna se o numero é decimal ou inteiro
"""

def main():
    #entrada
    numero = float(input("digite um numero"))
    #processamento
    if numero == int(numero) :
        print("inteiro")
    else :
        print("decimal")
    #saida

if __name__ == '__main__':
    main()
