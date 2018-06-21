def main():
    frase = input("digite uma frase: ")

    lista = frase.split()

    for palavra in lista :
        print(palavra)

if __name__ == '__main__':
    main()
