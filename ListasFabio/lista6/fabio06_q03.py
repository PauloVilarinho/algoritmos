def main():
    frase = input()

    lista = frase.split()

    nova_frase = ''

    for i in range(len(lista)):
        nova_frase += lista[i]


    print(nova_frase)

if __name__ == '__main__':
    main()
