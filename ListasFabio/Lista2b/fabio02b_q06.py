"""
	Questão: Lista 2b 06
	Descrição: receba 1 letra e retorna uma saudação
"""

def main():
    #entrada
    letra = input("qual seu turno?(M,V,N)")
    #processamento
    letra = letra.upper()
    if letra == "M" :
        print("Bom Dia")
    elif letra == "V" :
        print("Boa Tarde")
    elif letra == "N" :
        print("Boa noite")
    else :
        print("Valor Invalido.")
    #saida

if __name__ == '__main__':
    main()
