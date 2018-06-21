def main():
    frase = input("digite uma frase")

    nova_frase = ""

    caracteres_nao_alterados = "aeiou "

    for i in range(len(frase)):
        if frase[i] in caracteres_nao_alterados:
            nova_frase += frase[i]
        else :
            nova_frase += "#"

    print(nova_frase[::-1])

if __name__ == '__main__':
    main()
