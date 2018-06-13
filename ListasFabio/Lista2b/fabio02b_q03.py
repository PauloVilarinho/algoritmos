"""
	Questão: Lista 2b 03
	Descrição: receba uma letra e retorna se é vogal ou não
"""

def main():
    #entrada
    letra = input("digite uma letra")
    #processamento
    letra = letra.upper()
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U" :
        vogal = True
    else:
        vogal = False
    #saida
    if vogal :
        print("é vogal")
    else :
        print("é consoante")
    


if __name__ == '__main__':
    main()
