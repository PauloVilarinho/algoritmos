"""
	Questão: Lista 2b 02
	Descrição: receba 1 letra e retorne o sexo da letra .-.
"""

def main():
    #entrada
    letra = input("digite uma letra")
    #processamento

    letra = letra.upper()
    if letra == "F":
        sexo = "feminino"
    elif letra == "M" :
        sexo = "masculino"
    else :
        sexo = "invalido"
    #saida

    print("sexo %s" %sexo)

if __name__ == '__main__':
    main()
