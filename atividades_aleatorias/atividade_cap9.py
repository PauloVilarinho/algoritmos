def main():
    menu = "#### Word Play ###" \
           "\n 1 - palavras n+ caracteres" \
           "\n 2 - palavras sem letra e "\
           "\n 3 - palavras sem letras proibidas"\
           "\n 4 - palavras com letras permitidas"\
           "\n 5 - palavras com letras necessarias"\
           "\n 6 - palavras abcedarias"\
           "\n 0 - sair"

    while True :
        option = int(input(menu))
        if option == 0 :
            break
        elif  option == 1 :
            palavras_com_n_ou_mais_caracteres()
        elif option == 2 :
            palavras_sem_e()
        elif option == 3 :
            avoid()
        elif option == 4 :
            uses_only()
        elif option == 5 :
            uses_all()
        elif option == 6 :
            is_abcedarian()





def obter_arquivo():
    arquivo = open("words.txt")
    return arquivo

def palavras_com_n_ou_mais_caracteres():
    n = int(input("limite?"))
    arquivo = obter_arquivo()
    for i in arquivo :
        palavra = i.strip()
        if len(palavra) >= n :
            print(palavra)

def palavras_sem_e():
    arquivo = obter_arquivo()
    total = 0
    total_e = 0
    for i in arquivo:
        palavra = i.strip()
        total += 1
        if not("e" in palavra):
            print(palavra)
            total_e += 1
    percentagem = (total_e/total)*100
    print("percentagem é", percentagem,"%")

def avoid():
    arquivo = obter_arquivo()
    letras = input("digite as letras proibidas com 1 espaço entre elas").split()
    for i in arquivo:
        palavra = i.strip()
        for j in letras:
            if j in palavra :
                valido = False
                break
            valido = True
        if valido :
            print(palavra)

def uses_only():
    arquivo = obter_arquivo()
    letras = input("digite as letras permitidas com 1 espaço entre elas\n").split()
    for i in arquivo:
        palavra = i.strip()
        for j in palavra:
            if not(j in letras) :
                valido = False
                break
            valido = True
        if valido :
            print(palavra)

def uses_all():
    arquivo = obter_arquivo()
    letras = input("digite as letras necessarias com 1 espaço entre elas\n").split()
    for i in arquivo:
        palavra = i.strip()
        for j in letras:
            if not(j in palavra) :
                valido = False
                break
            valido = True
        if valido :
            print(palavra)

def is_abcedarian():
    arquivo = obter_arquivo()
    for i in arquivo:
        palavra = i.strip()
        valor = 0
        valido = True
        for j in palavra:
            novo_valor = ord(j)
            if novo_valor < valor:
                valido = False
                break
            valor = novo_valor
        if valido :
            print(palavra)


if __name__ == '__main__':
    main()
